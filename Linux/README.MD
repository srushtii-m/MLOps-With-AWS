### Directory:

pwd --> displays present working directory				
mkdir mydir  --> create a directory 				
cd mydir --> change directory				
ls --> lists contents of current directory				
ls -l --> list contents of current directory with detailed output				
ll --> list contents of current directory with detailed output					
cd <folder> 					
cd .. --> to come out of a directory 					
rm -r testdir --> to remove a directory					
`~` --> Home directory					
mkdir -p folder/subfolder/subfolder2 --> create parent and child directory						

### File Operations:				

touch test.txt --> creates a empty file 			
ls -l --> lists the contents in current directory					
echo "Print Output"												
echo "This is a text" > test.txt				
cat test.txt --> writes the content of file into terminal & exits				 
more test.txt --> writes the content of file on terminal page by page ( to move to next page need to hit space bar on keyboard )				
less test.txt --> open the file on terminal & can be read line by line (use arrows to scroll up & down) 				  
vi test.txt --> Visual Editor                                         
				This opens the file in read only mode			
				To edit the file, press 'i' on keyboard for INSERT mode & then you can write anything			
				once the text is entered, press 'ESC' on keyboard to return back on readonly mode			
				press ':wq' on keyboard -- to save & come out of the file			
				press ':q' on keyboard -- to come out of the file without saving			
				press ':wq!' on keyboard -- to save forcefully & come out of the file			
				press ':q!' on keyboard -- to come out of the file forcefully without saving			
rm test.txt --> To remove a file 		                           

### Copy/Rename/Move File:                                           

cp A.txt B.txt  -- makes a copy of A.txt names it to B.txt in current directory                                        
cp /home/A.txt /tmp/A.txt -- make a copy of A.txt to /tmp                                    
cp -r testdir/ newdir/ -- makes a copy of testdir & names it to newdir in current dirctory                           
cp -r /home/testdir /tmp/testdir -- makes a copy of testdir to /tmp                            

mv A.txt new.txt --- renames A.txt to new.txt in current path        
mv A.txt /tmp --- moves to A.txt to /tmp                   
mv testdir newdir -- renames testdir to newdir in current path 						                       
mv newdir /tmp --- moves newdir to /tmp path     			                 

Permissions:												

drwxrwxr-x or -rw-rw-r--   --> Read/Write/Execute Permission for a file or a directory in linux				
(1st value)manifoldailearning - owner of the file/directory			
(2nd value)manifoldailearning - group who owns file/directory 				
how to update the owner & group for a file/dir :					
chown ( change owner ) is the command to update the owners of dir/file				
chown owner:group filename/dirname						

-/d    ---> denotes if it is a file or directory ( - means file / d means directory ) 					
rwx    ---> means read,write & execute permissions for super user ( root )						
rw-    ---> means read,write permissions for the owner of the file ( ex: manifoldailearning as above )  				
r--    ---> means read only permissions for others ( whoever login to the machine ) 					

r  -- Permission to read the file.					
w  -- Permission to write (or delete) the file.					
x  -- Permission to execute the file, or, in the case of a directory, search it.					
						
