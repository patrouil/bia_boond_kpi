#!/usr/bin/env sh

rm log/*
rm ._* */._* */*/._*

tar --no-xattrs --no-acls --no-mac-metadata -cf package.tar *.py boond engine kpi mapper query log/ boondkpi.sh requirements.txt \
      conf/sample-config.json conf/logging.conf conf/Template-KPI.pptx

