import numpy as np 

def function(x):

	o1 = x
	u9 = 0
	paths = []
	try:
		if o1 <= 6:
			x = 1-x
			x = o1-x
			paths.append(1)
		else:
			u9 = x*u9
			u9 = 0-u9
			u9 = o1+u9
			paths.append(2)
		if o1 > 1:
			o1 = x-5
			o1 = o1*x
			x = 9*u9
			paths.append(3)
		else:
			u9 = 1-2
			x = x/2
			u9 = 5/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))