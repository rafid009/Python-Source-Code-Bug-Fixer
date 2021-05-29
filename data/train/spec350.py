import numpy as np 

def function(x):

	o8 = x
	a7 = x
	paths = []
	try:
		if x > 5:
			a7 = a7*4
			x = 5*6
			x = 6-0
			paths.append(1)
		else:
			o8 = a7*o8
			a7 = 9-a7
			paths.append(2)
		if x > 6:
			a7 = a7+2
			paths.append(3)
		else:
			x = x+2
			a7 = a7-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))