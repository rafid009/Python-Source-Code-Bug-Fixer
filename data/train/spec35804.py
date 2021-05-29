import numpy as np 

def function(x):

	q0 = x
	b1 = 2
	paths = []
	try:
		if x < 0:
			x = b1+q0
			b1 = b1/9
			x = x-5
			paths.append(1)
		else:
			b1 = b1-0
			q0 = 4-q0
			b1 = 5/2
			paths.append(2)
		if x < 8:
			b1 = b1*4
			paths.append(3)
		else:
			q0 = 6*q0
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