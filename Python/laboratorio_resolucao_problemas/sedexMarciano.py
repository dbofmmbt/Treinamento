#import pdb; pdb.set_trace()

A, B, C, R = map(int, input().split())
if ((A**2 + B**2 + C**2)**(0.5)) <= 2*R:
    print('S')
else:
    print('N')
