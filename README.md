# ngnkcart
Searchable database of snippets for [ngn/k](https://codeberg.org/ngn/k)  
Inspired by [aplcart](https://github.com/abrudz/aplcart)  
Join The APL Farm [discord](https://discord.gg/ZN9wVvpv) to contribute snippets,
or just PR them.  

## search 
Available at https://secwang.github.io/ngnkcart.  
The interface is a direct clone of APLcart, so the [usage instructions](https://github.com/abrudz/aplcart#usage) are the same.  
Alternatively, open [table.csv](https://github.com/secwang/ngnkcart/blob/main/table.tsv).  
Type in the github search box.  
You can add this file to your bookmarks.  

## design
All snippets are stored in the table.tsv file. Addition of snippets and maintenance happens there.  
Import the tsv into sqlite for fulltext search and format check.  
Goals:  
- [x] discord search and commit
- [x] cli search
- [x] searchable tsv page.
- [x] static web page

# commandline use  
Install [fzf](https://github.com/junegunn/fzf).  
add kcbin.sh to your $PATH, or just run as is (`./kcbin.sh` for a fuzzy search).  
