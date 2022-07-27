# -*- coding: utf-8 -*-
#
# python3-cookbook documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 19 03:21:45 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax', 'sphinx_multiversion']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
# source_parsers = {
#   '.md': 'recommonmark.parser.CommonMarkParser',
# }

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    # '.md': 'markdown',
}
# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'

# html_theme = 'default'
html_theme = 'sphinx_rtd_theme'


html_static_path = ['_static']

language = 'zh_CN'

latex_elements={# The paper size ('letterpaper' or 'a4paper').
'papersize':'a4paper',# The font size ('10pt', '11pt' or '12pt').
'pointsize':'12pt','classoptions':',oneside','babel':'',#必须
'inputenc':'',#必须
'utf8extra':'',#必须
# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont{WenQuanYi Micro Hei}
\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
\setCJKfamilyfont{song}{WenQuanYi Micro Hei}
\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
"""}



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# otherwise, readthedocs.org uses their theme by default, so no need to specify it
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

_exts = "../exts"
sys.path.append(os.path.abspath(_exts))

html_js_files = [
   'js/readmore.js',
    'js/baidutongji.js',
]


author = 'Henson'
copyright = '2022, HensonLab'


exclude_patterns = ['_build']
include_patterns = ['index/*']

master_doc = 'index'
project = '阿帆的学习笔记'

# Options for extensions.
html_baseurl = 'https://magic.iswbm.com'
html_extra_path = ["robots.txt"]

html_sidebars = {
    '**': [
        'versioning.html',
    ],
}
smv_latest_version = 'v1.0' 
sitemap_url_scheme = "{link}"

