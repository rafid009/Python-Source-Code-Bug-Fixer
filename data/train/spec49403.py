import numpy as np 

def function(x):

	x1 = 6
	f6 = x
	paths = []
	try:
		if f6 > 1:
			x = 5*4
			x = x+0
			paths.append(1)
		else:
			x = x1*f6
			x1 = x1-x1
			x = x/2
			paths.append(2)
		if x > 7:
			f6 = f6*9
			x1 = x1/2
			f6 = x*6
			paths.append(3)
		else:
			f6 = x*f6
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))