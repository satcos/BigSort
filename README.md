# BigSort
Sort files which are TeraBytes in Size

Python implementation of merge sort which can be used to sort files as big as TBs. The one of the major problem in sorting is holding the data in memory, so read file serially i.e. read line by line, once considerable amount of lines are obtained sort them in-memory and write to separate file. Continue to read from the main file where we left, do the above process till the file is over. Now we have multiple small files whose content are sorted. In order to merge them as single sorted file, created file read pointer to each small file, compare the content at header and write to final sorted file. 

A detailed tutorial is available at www.satcos.in/programming/BigSort.php
