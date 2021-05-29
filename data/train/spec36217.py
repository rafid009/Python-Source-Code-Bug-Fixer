import numpy as np 

def function(x):

	o8 = 0
	a2 = 8
	paths = []
	try:
		if a2 <= 5:
			x = x-0
			x = o8*0
			a2 = 6*o8
			paths.append(1)
		else:
			a2 = 1-0
			x = o8-2
			a2 = 4+x
			paths.append(2)
		if o8 <= 8:
			a2 = o8+2
			a2 = 3+o8
			o8 = o8+o8
			paths.append(3)
		else:
			x = 4/7
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