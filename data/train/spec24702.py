import numpy as np 

def function(x):

	b3 = 6
	l4 = 8
	paths = []
	try:
		if b3 <= 7:
			b3 = x/b3
			b3 = b3/4
			paths.append(1)
		else:
			x = x*1
			b3 = 0*b3
			l4 = x-l4
			paths.append(2)
		if l4 < 8:
			x = x+x
			l4 = 1*l4
			paths.append(3)
		else:
			l4 = x+x
			b3 = 0-x
			x = 2*2
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		b3 = l4**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))