Dotfiles: What they are, why you need one, where they live, how to do it?
#########################################################################
:tags: dotfiles, vim, bash, zsh, shell
:date: 2014-11-23

What they are
-------------

Dotfiles are configuration files that reside in your home (``~``) directory.
They are hidden files, preceded with a dot (``.``), that's why they're called **dotfiles** and
usually have a rc suffix (e.g. ``.bashrc``, ``.vimrc``).

It is usual to share dotfiles and learn from others.
This is an introductory article about them.

Why you need one
----------------

Setting up a development environment can be stressful and time-consuming.
Dotfiles are a great way to back up and bootstrap your development environment configuration.

Working in a machine without your aliases, shortcuts and vim plugins can be *very* unproductive.
I experiment this every time I need to work in someone's computer, for example.

Dotfiles are a great way to get your development enviroment configured fast and easily.

Where they live
---------------

Dotfiles must be shared.
Dotfiles are `meant to be forked <http://zachholman.com/2010/08/dotfiles-are-meant-to-be-forked/>`_.

As an example, I've discovered dotfiles after a suggestion from my colleague `Bruno Mentges <http://github.com/bmentges>`_. He was specially interested in vim configs and, for instance, used `nvie's vimrc <https://github.com/nvie/vimrc>`_ as inspiration.

The first thing I did was to fork his dotfiles.
By doing this I've discovered some vim configs I was not aware of.
Forking other people's dtofiles is a great way to learn from others.

Other great thing about hosting dotfiles on github is having a safe place to back them up.

All my dotfiles are in a `git repository <http://github.com/icaromedeiros/dotfiles>`_ linked to github and they are simply a link to the cloned github repository:

.. code-block:: guess

    ~/.vimrc -> ~/workspace/dotfiles/vim/.vimrc

Every configuration change is synced with the github repository.

How to do it
------------

At first, you must create your dotfiles like ``.zshrc`` and ``.vimrc`` with your customized settings.

It is good to have executable configuration appliers like shell scripts to do the symlink, install needed software, and so on.
In `my dotfiles <http://github.com/icaromedeiros/dotfiles>`_, I created a set of scripts and a Makefile to install my dotfiles and other environment must-haves.

.. code-block:: makefile

    # ...
    zsh:
        @sh zsh/install.sh
    # ...

In ``zsh/install.sh`` script, oh-my-zsh is installed, the ``.zshrc`` is symlinked in the home directory and a personalized theme is applied.

.. code-block:: sh

    #!/usr/bin/env bash
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

    echo "Installing oh my zsh..."
    curl -L http://install.ohmyz.sh | sh

    echo "Installing .zshrc"
    ln -sf $DIR/.zshrc ~/.zshrc

    echo "Installing zsh theme"
    cp $DIR/icaro.zsh-theme ~/.oh-my-zsh/themes/icaro.zsh-theme
    echo "Done."

A good way to keep dotfiles organized by topic, like `Zach Holman's dotfiles <https://github.com/holman/dotfiles>`_ or `mine <http://github.com/icaromedeiros/dotfiles>`_.

Today there are also tools and frameworks for making it faster to configure your environment like `rcm <https://github.com/thoughtbot/rcm>`_, `fresh <https://github.com/freshshell/fresh>`_, or `ghar <https://github.com/philips/ghar>`_.

Discover more
-------------

I've written a curated list about `dotfiles at zeef <https://dotfiles.zeef.com>`_.
It includes other introductory articles, and useful links for vim configuration, shell, great dotfiles examples and so on.
