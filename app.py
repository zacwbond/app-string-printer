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
  
text = append.append_efg(sys.argv[1])

print(ascii_iphone.format(align_text(text)))
