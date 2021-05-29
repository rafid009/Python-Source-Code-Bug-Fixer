import numpy as np 

def function(x):

	o5 = 4
	x3 = x
	paths = []
	try:
		if x < 4:
			x = o5*x
			x = 9/x
			paths.append(1)
		else:
			x = 3*4
			paths.append(2)
		if o5 > 3:
			x = 5-9
			x = x3-x
			paths.append(3)
		else:
			o5 = o5+6
			x = 1/o5
			x3 = x3/1
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))