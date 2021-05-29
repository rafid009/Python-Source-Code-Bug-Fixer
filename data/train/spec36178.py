import numpy as np 

def function(x):

	b2 = 7
	p7 = x
	paths = []
	try:
		if x >= 7:
			p7 = 0*p7
			x = b2-x
			paths.append(1)
		else:
			x = x-x
			x = x+2
			b2 = b2-x
			paths.append(2)
		if x >= 2:
			x = x+x
			paths.append(3)
		else:
			p7 = x/x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))