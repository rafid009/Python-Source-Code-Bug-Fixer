import numpy as np 

def function(x):

	n1 = x
	b6 = x
	paths = []
	try:
		if n1 < 3:
			x = b6+n1
			n1 = 9*n1
			n1 = x*n1
			paths.append(1)
		else:
			b6 = 4+b6
			x = x+x
			paths.append(2)
		if x > 1:
			b6 = b6*5
			n1 = n1-n1
			paths.append(3)
		else:
			b6 = b6*8
			n1 = b6/x
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))