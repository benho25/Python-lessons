# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:02:26 2019

@author: cho01
"""

"""
SIDE NOTES
Python programs are plain text files.
They have the .py extension to let everyone (including the operating system) know it is a Python program.
It’s common to write them using a text editor but we are going to use the Syder Notebook.
The bit of extra setup is well worth it because the Notebook provides code completion and other helpful features.
Notebook files have the extension .ipynb to distinguish them from plain-text Python programs.
Can export as “pure Python” to run from the command line.
"""

"""
FOR JUPYTER
The Anaconda package manager is an automated way to install the Jupyter notebook.
See the setup instructions for Anaconda installation instructions.
It also installs all the extra libraries it needs to run.
Once you have installed Python and the Jupyter Notebook requirements, open a shell and type:
$ jupyter notebook
This will start a Jupyter Notebook server and open your default web browser.
The server runs locally on your machine only and does not use an internet connection.
The server sends messages to your browser.
The server does the work and the web browser renders the notebook.
You can type code into the browser and see the result when the web page talks to the server.
This has several advantages:
You can easily type, edit, and copy and paste blocks of code.
Tab complete allows you to easily access the names of things you are using and learn more about them.
It allows you to annotate your code with links, different sized text, bullets, etc. to make it more accessible to you and your collaborators.
It allows you to display figures next to the code that produces them to tell a complete story of the analysis.

HOW is it Stored
The notebook file is stored in a format called JSON.
Just like a webpage, what’s saved looks different from what you see in your browser.
But this format allows Jupyter to mix source code, text, and images, all in one file.

CODE VS TEXT
Jupyter mixes code and text in different types of blocks, called cells. We often use the term “code” to mean “the source code of software written in a language such as Python”. A “code cell” in a Notebook is a cell that contains software; a “text cell” is one that contains ordinary prose written for human beings.


More information can be taken from http://swcarpentry.github.io/python-novice-gapminder/01-run-quit/index.html