Microformatos
#############
:date: 2009-09-03 02:52
:tags: microformats, rdfa, semantic web, linked data

`Microformatos <http://microformats.org/>`_ são conjuntos de formatos abertos usados para aumentar a capacidade semântica do HTML, adicionando metadados sobre contatos, feeds, eventos, etc.

.. figure:: images/microformats-logo.png
   :alt: Microformatos
   :class: align-center

Basicamente são usados em atributos (X)HTML como ``class`` e ``rel``.

Por exemplo, pode-se dizer que:

.. code-block:: html

    O avião Air France 447 caiu nas coordenadas
    <span class="geo">
     <span class="latitude">48.15</span>,
     <span class="longitude">-16.2342</span>
    </span>

Essa informação é lida por browsers, ferramentas de busca e outros sistemas que conseguem "entender" que aqueles dados são referentes a coordenadas geográficas.

Isso permite tarefas como:

* Indexar e recuperar consultas baseadas em coordenadas geográficas (num sistema de busca)

* Encontrar no mapa essas coordenadas oferecendo uma informação contextual que o site original pode não oferecer

* Exportar a informação para um dispositivo GPS

Uma grande aplicação recentemente anunciada que usa Microformatos é o `Google Rich Snippets <https://support.google.com/webmasters/answer/99170?hl=en>`_.

Snippets são aqueles resumos da página (geralmente contextualizados com a consulta) que aparecem nos resultados do Google abaixo dos links.

Rich Snippets são uma tentativa do Google de mostrar algo a mais que apenas o conTEXTO da sua consulta, e se valer de dados estruturados da página para mostrar por exemplo reviews e notas para produtos e serviços pesquisados.

.. figure:: images/rich-snippets.png
   :alt: Rich Snippets na página de resultados do Google
   :class: align-center

   Rich Snippets na página de resultados do Google

Páginas com snippets ricos tem maiores possibilidades de serem acesssadas, segundo experimentos deles.

Mas, para que as páginas apareçam com esses resumos melhorados, os webmasters devem incluir anotações em microformatos (ou `RDFa <http://rdfa.info/>`_) em suas páginas.

Alguns exemplos de microformatos:

* `hAtom`_ - para marcação de feeds Atom

* `hCalendar`_ - para eventos

* `hCard`_ - para informação de contatos, incluindo endereço, localização geográfica, etc.

* `hProduct`_ - para informações sobre produtos

* `hReview`_ - para reviews de livros, filmes, restaurantes, etc.

Saiba mais: http://microformats.org/

.. _hAtom: http://microformats.org/wiki/hatom
.. _hCalendar: http://microformats.org/wiki/hcalendar
.. _hCard: http://microformats.org/wiki/hcard
.. _hProduct: http://microformats.org/wiki/hproduct
.. _hReview: http://microformats.org/wiki/hreview
