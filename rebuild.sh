#!/bin/bash
echo -e ".mode tabs\n.output raw.tsv\nselect * from raw;\n.output stdout\n" | sqlite3 table.sqlite3
rm table.sqlite3
cat cart.ddl | sqlite3 table.sqlite3
echo -e ".mode tabs\n.import table.tsv cart" | sqlite3 table.sqlite3
sqlite3 table.sqlite3 "select count(*) from cart"

