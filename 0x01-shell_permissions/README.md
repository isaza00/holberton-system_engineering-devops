This project have the exercises fo project 1 of shell permissions.
whoami :displays current user
  su - user2 :changes user to user2
    chmod change permissions of a file
      chmod 600 file_name: read and write permission for owner but private for others
        chown user_name file: change the owner of a file
	  chgrp group_name file: change the group ownership of file


	    - rwx       rwx       rwx
	        (f_owner) (g_owner) (all_users)
		    rwx 111 = 7
		        rw- 110 = 6
			    r-x 101 = 5
			        r-- 100 = 4
				    -wx 011 = 3
				        -w- 010 = 2
					    --x 001 = 1
					      for directories:
					        r: allows content of dir to be listed if x is set
						  w: allows files withint the dir created, deleted or rename if x is set
						    x: allows a dir to be entered
