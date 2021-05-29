import numpy as np 

def function(x):

	o5 = 4
	a7 = 4
	paths = []
	try:
		if x < 0:
			o5 = o5/a7
			o5 = 0*o5
			o5 = o5*3
			paths.append(1)
		else:
			o5 = x*o5
			x = 2-o5
			paths.append(2)
		if o5 >= 9:
			x = o5-x
			x = a7+a7
			o5 = 8+o5
			paths.append(3)
		else:
			a7 = a7+a7
			o5 = 0*o5
			a7 = 5+a7
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