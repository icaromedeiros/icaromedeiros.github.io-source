De volta
########
:date: 2014-08-10
:tags: blogging
:lang: pt
:slug: im-back

Olá a todos.

Eu blogava `aqui <http://kirux.wordpress.com>`_ durante meu mestrado [2008-2009], apenas em português.

Agora eu tenho esse novo blog orgulhosamente construído com `Pelican <http://blog.getpelican.com/>`_, `Python <http://python.org>`_, `RestructuredText <http://sphinx-doc.org/rest.html>`_, e a *fantástica ferramenta de deploy de páginas estáticas* que o `Github Pages <http://pages.github.com>`_ oferece.

**Um pouco sobre ferramentas de blog**

Alguns dos meus requisitos não formais para uma ferramenta de blog que me fizeram tomar essas escolhas:

#. Eu não quero emails, mídia social ou conexão com a Internet atrapalhando a escrita.
#. Eu não quero uma ferramenta WYSIWYG, um `grande, porém simples editor de texto <http://www.vim.org>`_ funcionará.
#. Eu quero ter páginas estáticas e controle do HTML final.
#. Eu quero ter deploys fáceis.
#. Eu quero importar meus posts antigos facilmente.
#. Eu quero ter internacionalização (escrever em inglês e português).
#. Eu quero escrever anotação semântica nos posts (usando Mcriodata e `schema.org <http://schema.org>`_ facilmente).
#. Eu quero que o blog seja responsivo, funcionando bem em dispositivos móveis.

`Wordpress <http://wordpress.org>`_ é suficiente pra maioria das pessoas mas falha nos itens 1, 2 e 3.

`Jekyll <http://jekyllrb.com/>`_/`Octopress <http://octopress.org/>`_ parecia uma opção viável desde o começo, mas Python é uma barreira de entrada menor pra mim do que Ruby, especialmente pra escrever microdata (item 7), até porque já existe um `plugin <https://github.com/noirbizarre/pelican-microdata>`_.

Falando em microdata, eu `melhorei o plugin pelican-microdata <http://github.com/icaromedeiros/pelican-microdata>`_ um pouco.

PS: Na verdade, sobre o item 6, foi um pouco frustrante a dificuldade em configurar o plugin `i18n subsites <https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites>`_.
Eu simplesmente desisti e usei apenas as traduções intra-artigos.
