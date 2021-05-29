import numpy as np 

def function(x):

	x3 = 7
	o6 = 7
	paths = []
	try:
		if x > 2:
			x3 = x3+3
			paths.append(1)
		else:
			o6 = o6-1
			o6 = x*8
			x = x*9
			paths.append(2)
		if x > 7:
			x3 = x3/4
			x3 = x3-4
			paths.append(3)
		else:
			x = 8*x
			o6 = o6+x3
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