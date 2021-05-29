import numpy as np 

def function(x):

	b4 = x
	n0 = x
	paths = []
	try:
		if n0 < 6:
			x = x+x
			paths.append(1)
		else:
			x = n0*5
			b4 = 4/n0
			paths.append(2)
		if n0 >= 8:
			b4 = 1+b4
			paths.append(3)
		else:
			n0 = n0/4
			b4 = b4+3
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))