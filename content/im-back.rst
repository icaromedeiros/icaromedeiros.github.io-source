I'm back
########
:date: 2014-08-10
:tags: blogging, python, pelican
:slug: im-back

Hi folks.

I have blogged `elsewhere <http://kirux.wordpress.com>`_ during my Master's [2008-2009], in portuguese.

Now I have this new blog proudly built using `Pelican <http://blog.getpelican.com/>`_, `Python <http://python.org>`_, `RestructuredText <http://sphinx-doc.org/rest.html>`_, and the *awesome ultimate blogging deploy system* that `Github Pages <http://pages.github.com>`_ offers.

**A few words about blogging tools**

Some of my not-so-formal requirements for a blogging tool that made me did these choices:

#. I don't want emails, social media, or internet connection getting in the way of writing.
#. I don't need a WYSIWYG tool, a `simple but great text editor <http://www.vim.org>`_ will work.
#. I want static pages and control the HTML output.
#. I want a smooth deploy.
#. I want to import my old posts nicely.
#. I want i18n (i.e. write both in `en` and `pt-br`).
#. I want to write semantic annotations in my posts (using Microdata and `schema.org <http://schema.org>`_ easily).
#. I want my blog to be responsive, working nicely in mobile devices.

`Wordpress <http://wordpress.org>`_ is enough for most people, but basically fails in items 1, 2, 3.

`Jekyll <http://jekyllrb.com/>`_/`Octopress <http://octopress.org/>`_ seemed  programmer-friendly from the start, but Python is a low entry barrier for me than Ruby, specially for implementing microdata semantic annotation (item 7), as there is a `plugin <https://github.com/noirbizarre/pelican-microdata>`_ already.

Speaking of microdata, I just `improved pelican-microdata <http://github.com/icaromedeiros/pelican-microdata>`_ a little.

PS: In fact, in item 6, it was a little bit frustrating the difficult of configuring `i18n subsites <https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites>`_ plugin.
I just gave up and just used intra-article translations.
