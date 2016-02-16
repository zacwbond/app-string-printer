
# Because I am an idiot and used dashes in the name...
import sys
from lib import append

ascii_iphone = '''
     ------------------------
     |                      |
     |                      |
     |                      |
     |         {}
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |        (    )        |
     |                      |
     ------------------------
'''

def align_text(s):
  return s + ' ' * (13 - len(s)) + '|'
  


print(ascii_iphone.format(align_text(append.append_bcd(sys.argv[1]))))
