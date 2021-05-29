import numpy as np 

def function(x):

	f5 = x
	n1 = x
	paths = []
	try:
		if x < 9:
			n1 = x-5
			f5 = f5/8
			paths.append(1)
		else:
			f5 = x+7
			x = x+4
			paths.append(2)
		if f5 > 8:
			x = x*4
			x = 1-9
			paths.append(3)
		else:
			f5 = 9/x
			x = x-4
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