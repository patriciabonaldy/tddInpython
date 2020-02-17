#!/bin/bash

#nosetests --with-coverage --cover-erase  --cover-html
#firefox cover/index.html 

set -e
nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-xml