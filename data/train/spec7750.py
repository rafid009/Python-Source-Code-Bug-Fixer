import numpy as np 

def function(x):

	n1 = x
	b6 = 2
	paths = []
	try:
		if x < 5:
			b6 = x-x
			paths.append(1)
		else:
			n1 = n1-2
			x = 4*9
			paths.append(2)
		if n1 < 5:
			b6 = n1/6
			n1 = 0+1
			paths.append(3)
		else:
			n1 = 5/n1
			b6 = 1*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))