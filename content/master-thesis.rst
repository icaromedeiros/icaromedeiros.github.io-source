Master thesis
#############
:date: 2009-09-23 15:27
:author: Icaro Medeiros
:tags: folksonomy, information retrieval, machine learning, social tagging, tag suggestion
:slug: master-thesis

Bom, o assunto da dissertação: `Folksonomias`_ e Sugestão de tags.

Construí um sistema que extraiu dados do Delicious e depois usei técnicas de RI, AM e outras coisas.
Usei como base da sugestão de tags pra páginas Web o conteúdo textual, páginas vizinhas (inbound pages) (80% implementado) e informação do WordNet e ontologias.

No final faço uma comparação entre as tags que sugeri e as tags do Delicious pra dar uma medida quantitativa do quanto o sistema é bom e
uma análise do comportamento do usuário (p. ex. que tipo de tags o sistema não consegue sugerir: "semweb" e "webdev").

.. figure:: images/tagcloud1.gif
   :alt: Nuvem de tags
   :class: align-center

   Nuvem de tags

Boa noite e boa sorte (pra mim)!

.. _Folksonomias: http://en.wikipedia.org/wiki/Folksonomy
