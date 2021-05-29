import numpy as np 

def function(x):

	b4 = x
	o1 = 1
	paths = []
	try:
		if x >= 3:
			o1 = o1*3
			b4 = b4/8
			x = x/3
			paths.append(1)
		else:
			o1 = o1*7
			paths.append(2)
		if o1 >= 0:
			o1 = o1+b4
			o1 = 1/o1
			b4 = b4-8
			paths.append(3)
		else:
			o1 = o1-x
			o1 = 1-3
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