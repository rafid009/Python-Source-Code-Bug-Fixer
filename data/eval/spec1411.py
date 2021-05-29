import numpy as np 

def function(x):

	o1 = x
	e4 = x
	paths = []
	try:
		if e4 < 4:
			o1 = o1/6
			x = x/6
			x = x+x
			paths.append(1)
		else:
			x = o1-x
			o1 = 5*3
			paths.append(2)
		if e4 < 9:
			o1 = o1*o1
			o1 = o1-8
			paths.append(3)
		else:
			e4 = 8-o1
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