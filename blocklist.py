"""
blocklist.py

This file contains the blocklist of the JWT tokens. It will be imported by app and the logout
resource so that tokens can be added to the blocklist when the user logs out.

"""

# This should normally be a database to store the blocklist, not a python set
BLOCKLIST = set()