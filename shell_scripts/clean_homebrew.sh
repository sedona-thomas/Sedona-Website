#! /bin/sh

brew bundle dump
brew bundle --force cleanup

brew doctor

brew cleanup
rm -rf $(brew --cache)

