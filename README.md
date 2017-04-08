# cloud_storage_crawler
1. cloud_storage_crawler will have GUI interface
2. cloud_storage_crawler periodically crawl meta data store in the database
3. It will help storage admin/User to maintain file for archive or compress and backup

Pattern design
    Composite design pattern can be used to collect meta information for all files

two different type of child either it is directory or file
directory will have child of directory or file
file do not have child

                     ---------
                    |directory|
                  /  ---------
                 /        |
             ------     ---------
    .  ..   |file  |   | directory|
             ------     ----------


fs_crawler --config <config file>

