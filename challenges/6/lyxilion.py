"""
Weekly Challenge: 6

Discord username: Lyxilion#4363

Yes, a oneliner again...
"""

txt = 'Hello World'

swapcase = lambda txt : "".join([e.lower() if (e.isupper()) else e.upper() for e in txt])

print(swapcase(txt))
