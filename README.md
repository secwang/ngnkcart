# ngnkcart
inspired by [aplcart](https://github.com/abrudz/aplcart) 


# design
maintain the table.tsv file.  
import tsv into sqlite for fulltext search and rank.  
use sql.js-httpvfs on github pages.  (TODO)
provide a discord bot for search.

# convert tsv into sqlite3
```
sqlite3 table.sqlite3
.mode tabs  
.import table.tsv cart  
```
