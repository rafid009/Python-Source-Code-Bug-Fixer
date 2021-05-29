import numpy as np 

def function(x):

	n1 = 8
	b3 = 8
	paths = []
	try:
		if n1 <= 7:
			n1 = 4*n1
			paths.append(1)
		else:
			b3 = n1*9
			n1 = n1*x
			paths.append(2)
		if x >= 0:
			x = n1-x
			b3 = b3-1
			n1 = n1-2
			paths.append(3)
		else:
			b3 = b3/n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))