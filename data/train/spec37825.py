import numpy as np 

def function(x):

	b1 = x
	n4 = 0
	paths = []
	try:
		if b1 <= 2:
			n4 = n4-5
			paths.append(1)
		else:
			n4 = n4-x
			b1 = b1-8
			paths.append(2)
		if x > 6:
			x = 6*x
			b1 = b1+7
			x = 5+0
			paths.append(3)
		else:
			n4 = b1-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))