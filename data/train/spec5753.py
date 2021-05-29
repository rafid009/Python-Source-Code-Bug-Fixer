import numpy as np 

def function(x):

	h5 = x
	o1 = 8
	paths = []
	try:
		if o1 > 7:
			x = 3*2
			o1 = 6-7
			paths.append(1)
		else:
			o1 = 0/6
			o1 = o1+h5
			o1 = o1*x
			paths.append(2)
		if x > 2:
			o1 = o1*h5
			o1 = 8-8
			x = 4-8
			paths.append(3)
		else:
			o1 = 0/o1
			x = 8-9
			h5 = 7/h5
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