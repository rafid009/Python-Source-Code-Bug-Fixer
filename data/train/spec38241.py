import numpy as np 

def function(x):

	o1 = 7
	x8 = x
	paths = []
	try:
		if o1 > 3:
			x = x-o1
			x8 = 1*8
			o1 = x+x8
			paths.append(1)
		else:
			o1 = x8-x8
			paths.append(2)
		if x8 > 2:
			x8 = x8/2
			x = x+2
			paths.append(3)
		else:
			x = x/6
			x = 5/4
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