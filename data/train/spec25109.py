import numpy as np 

def function(x):

	o1 = x
	x8 = 1
	paths = []
	try:
		if o1 >= 9:
			o1 = x8+o1
			x = 0*3
			o1 = x8-o1
			paths.append(1)
		else:
			x = x*8
			x8 = 5+1
			paths.append(2)
		if x > 7:
			x = 7*3
			paths.append(3)
		else:
			o1 = o1-o1
			x = o1-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))