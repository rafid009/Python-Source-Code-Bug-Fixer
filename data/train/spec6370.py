import numpy as np 

def function(x):

	o5 = x
	j8 = x
	paths = []
	try:
		if o5 > 8:
			j8 = o5*j8
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if o5 >= 9:
			x = x/o5
			paths.append(3)
		else:
			j8 = j8/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))