import numpy as np 

def function(x):

	a8 = x
	o8 = x
	x = 3
	paths = []
	try:
		if a8 <= 5:
			a8 = a8*4
			x = x*a8
			o8 = a8-6
			paths.append(1)
		else:
			o8 = x+o8
			a8 = o8+2
			x = a8-x
			paths.append(2)
		if a8 <= 7:
			a8 = 3/x
			paths.append(3)
		else:
			x = 5+o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))