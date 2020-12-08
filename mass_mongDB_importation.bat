@echo off
cd "C:\Program Files\MongoDB\Server\4.2\bin"

FOR %i IN (C:\Users\radfi\Downloads\noncomm_use_subset.tar\noncomm_use_subset\*.json) DO mongoimport --db CORD19 --collection covid_live_dataset --type json --file %i