import numpy as np 

def function(x):

	o6 = x
	z7 = 7
	x = 5
	paths = []
	try:
		if o6 > 9:
			x = x*4
			o6 = o6/2
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if o6 <= 2:
			x = x+z7
			paths.append(3)
		else:
			o6 = o6*x
			o6 = o6+z7
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))