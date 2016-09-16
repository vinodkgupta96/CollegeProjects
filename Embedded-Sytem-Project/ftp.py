import pysftp
import sys

# Defines the name of the file for download / upload
remote_file = sys.argv[1]

srv = pysftp.Connection(host="students.iitmandi.ac.in", username="v_kumar",
password="#define pie 3.14")

# Download the file from the remote server
#srv.get(remote_file)

# To upload the file, simple replace get with put. 
srv.put(remote_file)

# Closes the connection
srv.close()