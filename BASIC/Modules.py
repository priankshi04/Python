# Modules - importing function from another file
from wsgiref.simple_server import server_version

from dog import bark
bark() # helps to take out specific fn from files
# we can also create a lib by creating a folder and in subfolder create functions
from lib import dog
# python provides many functions from different modules
math for math utilities
re for regular expressions
json to work with JSON
datetime to work with dates
sqlite3 to work with SQLite
os for Operating System utilities
random for random number generators
statistics for statistics utilities
requests to perform HTTP network utilities
http to create HTTP servers
urllib to manage URLs