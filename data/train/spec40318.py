import numpy as np 

def function(x):

	b4 = x
	x5 = x
	paths = []
	try:
		if x5 <= 0:
			x = x-1
			paths.append(1)
		else:
			x5 = 2*1
			x5 = 0*x5
			x5 = 1-x5
			paths.append(2)
		if x > 7:
			x = 9/x
			paths.append(3)
		else:
			b4 = 2-x
			x5 = 5-7
			b4 = 0/b4
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))