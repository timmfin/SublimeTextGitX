SublimeTextGithubDesktop
===============

Very simple plugin to open Github desktop (https://desktop.github.com/) from Sublime Text 2 and 3 (http://www.sublimetext.com/).

Installing
----------

**Using Git:** Clone the repository in your Sublime Text Packages directory and restart Sublime Text:

    git clone https://github.com/timmfin/SublimeTextGithubDesktop

**Using the Package Control plugin:** The easiest way to install SublimeTextGithubDesktop is through Package Control,
which can be found at http://wbond.net/sublime_packages/package_control .

Once you install Package Control, restart Sublime Text 2 and open the Command Palette.

Select "Package Control: Install Package", wait while Package Control fetches the latest package list,
then select SublimeTextGithubDesktop when the list appears.

The advantage of using this method is that Package Control will automatically keep this plugin up to date.

Usage
-----

Open GitX and enable terminal usage by clicking on the GitX menu and then on ``Enable Terminal Usage...``;
GitX will create an executable named ``github`` inside ``/usr/local/bin``.

Open the command palette and execute the ``Github desktop: Open`` command to open the GIT repository
in which the currently opened file is located.

Sample user key binding to execute the command::

    { "keys": ["super+."], "command": "github_desktop_open" }

Configuration
-------------

Additional settings can be configured in the User File Settings:

``github_path``: the path to the ``github`` executable (default: ``"/usr/local/bin/github"``)

Changelog
---------
v0.1 (01-04-2011):

* Initial version

v0.2.0 (01-16-2014):

* Updated README about ST3 compatibility

License
-------
See the LICENSE.txt file.
