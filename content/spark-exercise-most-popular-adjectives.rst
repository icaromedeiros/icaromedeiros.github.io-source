An exercise to learn Spark: most popular adjectives by decade
#############################################################
:tags: big data, spark, python
:date: 2015-XX-YY


!! TODO CITAR !!

J. Michel, Y. Shen, A. Aiden, A. Veres, M. Gray, Google Books Team, J. Pickett, D. Hoiberg,
D. Clancy, P. Norvig, J. Orwant, S. Pinker, M. Nowak, and E. Aiden. Quantitative analysis of culture using millions of digitized books. Science, 331:176–182, 2011.

While I was learning spark by reading `Learning Spark <http://shop.oreilly.com/product/0636920028512.do>`_,
I realized that something was missing:
to be sure that I was really learning,
I needed to practice but the book did not provided any incentive to that (despite of being a good book).

It was also difficult to find Spark exercises on the Web.
I've tried to do `AMP Camp 3 exercises <http://ampcamp.berkeley.edu/3/exercises/launching-a-bdas-cluster-on-ec2.html>`_ on Amazon EC2,
but couldn't setup the cluster.
Maybe because the AMI (Amazon Machine Image) is old and somehow incompatible.

Then I decided I was going to search for public datasets and find some challenge to pursue.

!! TODO FOTO DO RESULTADO !!

The problem
-----------

My goal was to solve some problem involving basic data operations such as counting, aggregation,
grouping, sorting, etc.

I've came across `Google ngram viewer <http://storage.googleapis.com/books/ngrams/books/datasetsv2.html>`_ when checking `Amazon datasets <aws.amazon.com/datasets>`_.
It is a dataset of n-grams, `part-of-speech tags <https://en.wikipedia.org/wiki/Part-of-speech_tagging>`_ and their usage,
extracted from 8 millions of scanned books dating from the 16th century until recent days.

The format is quite simple,
a TSV with (word_POS, year, match count, volume count) tuples.
Match count is the number of times that word with that POS tag appeared that year.
Volume count is the number of books in which that word with that POST tag appeared that year.

.. code-block:: tsv

   YOUNG_ADJ    2006    693     502
   YOUNG_ADJ    2007    800     548
   YOUNG_ADJ    2008    1574    1066

So the problem I've proposed to myself was:
Get the most popular adjectives in English through decades using Google books dataset.
It is an interesting yet relatively easy problem to solve with basic data operations using Spark!

The code
--------

All the code is hosted on my github.
Feel free to download and try it out.

Step 1 - Downloading the dataset
--------------------------------

There is a simple script to download the data. It is run with:

.. code-block:: shell

   $ python download_dataset.py

It downloads all the data with the format ``googlebooks-eng-all-1gram-20120701-X.gz`` where X is the letter and,
saves the file in ``data`` directory,
and unzipped its contents.

I've only used unigrams because it is rare to have adjectives with 2 grams or more.
The dataset has 23G and 1.2 billion lines.

Step 2 - Filtering out adjectives
---------------------------------

In order to make testing the other steps with a smaller dataset,
the first step was to filter out adjectives in all files and saving
in a intermediary result with just the adjectives.

.. code-block:: python

   files_rdd = sc.textFile("googlebooks-eng-all-1gram-20120701-*")
   adjectives_rdd = files_rdd.filter(lambda line: line.split("\t")[0].endswith("_ADJ"))
   adjectives_rdd.saveAsTextFile("1gram-adjectives-english.txt")

The code is almost self explanatory.
All text files representing unigram adjectives are loaded in line 1.
In line 2, adjectives are filtered and assigned to `adjectives_rd` variable.
Finally, the resulting RDD is saved,
consisting of a 1.8G file with 86 million entries.

Step 2 - Loading and processing file lines
------------------------------------------

With a file containing only the adjectives,
we need to load it and process its lines to transform it in a `RDD <http://spark.apache.org/docs/latest/quick-start.html>`_ suitable for data transformations.

.. code-block:: python

    def process_line(line):
        word, year, match_count, vol_count = line.split("\t")

        word = word.split("_")[0]
        decade = "{0}*".format(year[:-1])
        match_count = int(match_count)
        vol_count = int(vol_count)

        return ((decade, word), (match_count, vol_count))

    adjectives_rdd = sc.textFile("1gram-adjectives-english.txt")
    mapped_decade = adjectives_rdd.map(process_line)

After loading the file into a RDD (line 11),
we map each line to ``process_line`` function (lines 1-9).

After spliting by tab[ref]As the dataset is a composed of `TSV files <http://storage.googleapis.com/books/ngrams/books/datasetsv2.html>`_.[/ref] (line 2),
the ``_ADJ`` suffix is removed and
in line 5 the year is transformed in decade ``(2015 -> 201*)``.

The returned structure is a tuple specifically engineered to contain the key ``(decade, word)`` to aggregate the records. An example of the function input and output is shown below.

.. code-block:: python

    >>> process_line("young_ADJ\t2015\t2\t1")
    (("young", "201*"), (2, 1))


Step 3 - Aggregating by decade
------------------------------

Records with ``(decade, word)`` as key can then be reduced to get the summed values for a decade.
The code belows does this process.

.. code-block:: python

    word_counts = mapped_decade.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
    decade_counts = word_counts.map(lambda x: (x[0][0], (x[0][1], x[1][0], x[1][1])))
    decade_counts = decade_counts.groupByKey().sortByKey()

In line XXX, we sum the volume and match count with with the same ``(decade, word)``.
After, we map the ``RDD`` to make only ``decade`` as key.

The resulting RDD is like ``[(decade, [(word, match_by_decade, vol_by_decade), ...])]``.
Finally, in line XXX, the records are groupped and sorted by decade.


Step 4 - Sorting the values for each decade
-------------------------------------------

We now have a RDD with records in ``decade, [(word, match count, volume count)]`` format.
The list of words and counts in the values are not sorted.
But we want the 10 most popular adjectives by matchs and volumes.

This is how we do that

.. code-block:: python

    top_by_match = []
    top_by_vol = []

    map(sort_and_add_to_result, decade_counts.collect())

    def sort_and_add_to_result(decade):
        global top_by_match, top_by_vol

        top_matchs_decade = sc.parallelize(decade[1]).sortBy(lambda x: x[1], ascending=False).take(10)
        top_vols_decade = sc.parallelize(decade[1]).sortBy(lambda x: x[2], ascending=False).take(10)
        top_by_match.append((decade[0], top_matchs_decade))
        top_by_vol.append((decade[0], top_vols_decade))


We need to iterate through the values of the RDD and then sort the values to

# rdd.foreach is not used because sc.parallelize cannot be called in a transformation

Step 5 - Results and plotting
-----------------------------



Summing up
-------------------

I was writing the challenge using simple RDD transformations.
With the feeling that the code was convoluted and not so readable.

I've then tried to use DataFrames (even updating Spark 1.4 to 1.5) and the experience was great.
You can check the old code using only RDDs here.
Spoiler: the code is more extense (two times longer), less elegant, and less readable.

I want to hear from you if there is a better more elegant or faster way to perform this process...


(REMOVER ISSO???) - trying to use amp camp cluster setup on amazon ec2, ended up $40 dollar on amazon for nothing
- not using unit tests from the start, include link to gist
