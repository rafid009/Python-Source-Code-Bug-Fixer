import numpy as np 

def function(x):

	k1 = x
	l4 = 8
	x = x
	paths = []
	try:
		if k1 > 9:
			k1 = 2*2
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if k1 >= 3:
			l4 = l4+3
			k1 = l4+x
			l4 = l4-k1
			paths.append(3)
		else:
			x = 9+x
			x = x+k1
			k1 = 1+k1
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))