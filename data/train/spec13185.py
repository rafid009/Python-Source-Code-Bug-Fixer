import numpy as np 

def function(x):

	b6 = x
	x1 = 2
	paths = []
	try:
		if b6 > 0:
			x1 = 3*x1
			paths.append(1)
		else:
			x = x/x
			x1 = x1+2
			b6 = b6*8
			paths.append(2)
		if x1 <= 2:
			x = x1-x
			b6 = b6*b6
			x1 = 8*x1
			paths.append(3)
		else:
			x1 = x1/x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x1 = b6**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))