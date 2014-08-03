Microformatos
#############
:date: 2009-09-03 02:52
:author: Icaro Medeiros
:tags: microformats, rdfa, semantic web, linked data
:slug: microformatos

Microformatos são conjuntos de formatos abertos usados para aumentar a capacidade semântica do (X)HTML, adicionado metadados sobre contatos, feeds, eventos, etc.

.. figure:: images/microformats-logo.png
   :class: align-center

Basicamente são usados em atributos (X)HTML como class e rel, sim, funciona com uma gambiarra do jeito que deu pra fazer.

Por exemplo, pode-se dizer que (Exemplo Wikipédico):

| [sourcecode language='html']
|  O avião Air France 447 caiu nas coordenadas
| 
|  48.15,
|  -16.2342
| 
|  [/sourcecode]

Essa informação é lida por browsers, ferramentas de busca e outros
sistemas que conseguem "entender" que aqueles dados são referentes a
coordenadas geográficas. Isso permite tarefas como:

    * Indexar e recuperar consultas baseadas em coordenadas geográficas (num sistema de busca)

    * Encontrar no mapa essas coordenadas oferecendo uma informação contextual que o site original pode não oferecer

    * Exportar a informação para um dispositivo GPS


Uma grande aplicação recentemente (? Março) anunciada que usa
Microformatos é o Google Rich Snippets. Primeiramente, snippets são
aqueles resumos da página (geralmente contextualizados com a consulta)
que aparecem nos resultados do Google abaixo dos links. Rich Snippets é
uma tentativa do Google de mostrar algo a mais que apenas o conTEXTO da
sua consulta, e se valer de dados estruturados da página para mostrar
por exemplo reviews e notas para produtos e serviços pesquisados.

.. figure:: images/rich-snippets.png
   :alt: Rich Snippets na página de resultados do Google
   :class: align-center

   Rich Snippets na página de resultados do Google

Páginas com snippets ricos tem maiores possibilidades de serem
acesssadas, segundo experimentos deles. Mas, para que as páginas
apareçam com esses resumos melhorados, os webmasters devem incluir
anotações em microformatos (ou RDFa, tema do próximo post SÉRIO daqui)
em suas páginas. Acho a iniciativa válida, mas ninguém tá com esse tempo
de fazer isso na mão, ferramentas de edição que extraiam informação e
detectem candidatos pra esses formatos são bem-vindas (quer ficar rico?
fica a dica). Além disso a propaganda do tema ainda tá fraca, o culto é
muito segregado e só tem uns bravos defensores, e não a W3C por trás.

Alguns exemplos de microformatos

    * `hAtom`_ - para marcação de feeds Atom

    *  `hCalendar`_ - para eventos

    *  `hCard`_ - para informação de contatos, incluindo endereço, localização geográfica, etc.

    *  `hProduct`_ - para informações sobre produtos

    *  `hReview`_ - para reviews de livros, filmes, restaurantes, etc.

Saiba mais: http://microformats.org/

.. _hAtom: http://microformats.org/wiki/hatom
.. _hCalendar: http://microformats.org/wiki/hcalendar
.. _hCard: http://microformats.org/wiki/hcard
.. _hProduct: http://microformats.org/wiki/hproduct
.. _hReview: http://microformats.org/wiki/hreview
