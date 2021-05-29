import numpy as np 

def function(x):

	j8 = x
	o6 = 0
	paths = []
	try:
		if o6 > 3:
			x = 9-1
			o6 = o6+3
			j8 = j8+j8
			paths.append(1)
		else:
			x = j8/x
			x = 2-x
			o6 = 8+j8
			paths.append(2)
		if o6 >= 2:
			x = j8*x
			paths.append(3)
		else:
			x = 0-6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))