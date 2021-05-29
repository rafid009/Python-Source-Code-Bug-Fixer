import numpy as np 

def function(x):

	x1 = x
	o1 = 6
	paths = []
	try:
		if o1 <= 0:
			x = x*9
			x1 = x1*x
			paths.append(1)
		else:
			o1 = x1*o1
			paths.append(2)
		if x1 <= 1:
			x = 5+x
			o1 = 5+x
			paths.append(3)
		else:
			x = x/9
			o1 = 5/o1
			x1 = x-x1
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