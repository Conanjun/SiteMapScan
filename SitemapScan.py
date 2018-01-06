#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
HTCAP - beta 1
Author: filippo.cavallarin@wearesegment.com

This program is free software; you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation; either version 2 of the License, or (at your option) any later 
version.
"""

from __future__ import unicode_literals
import sys
import os
import datetime
import time
import getopt

from core.lib.utils import *
from core.crawl.crawler import Crawler
from core.scan.scanner import Scanner

from core.util.util import Util

reload(sys)
sys.setdefaultencoding('utf8')


def logo():
    print(
        '''
  mmmm    "      m                                 mmmm                      
 #"   " mmm    mm#mm   mmm   mmmmm   mmm   mmmm   #"   "  mmm    mmm   m mm  
 "#mmm    #      #    #"  #  # # #  "   #  #" "#  "#mmm  #"  "  "   #  #"  # 
     "#   #      #    #""""  # # #  m"""#  #   #      "# #      m"""#  #   # 
 "mmm#" mm#mm    "mm  "#mm"  # # #  "mm"#  ##m#"  "mmm#" "#mm"  "mm"#  #   # 
                                           #                                 
                                           "                                 
                                           
 Authors: Conan0xff Wha000tif Konakona
 Version: 1.0
 
 
 usage: SitemapScan <command>
 commands: 
    crawl                  run crawler
    scan                   run scanner
    util                   run utility
        '''
    )


if __name__ == '__main__':
    logo()
    if len(sys.argv) < 2:
        logo()
        sys.exit(1)

    elif sys.argv[1] == "crawl":
        Crawler(sys.argv[2:])
    elif sys.argv[1] == "scan":
        Scanner(sys.argv[2:])
    elif sys.argv[1] == "util":
        Util(sys.argv[2:])
    else:
        logo()
        sys.exit()

    sys.exit(0)
