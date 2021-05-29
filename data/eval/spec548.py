import numpy as np 

def function(x):

	o6 = x
	r6 = 1
	paths = []
	try:
		if o6 < 8:
			r6 = 8*r6
			r6 = 5+r6
			paths.append(1)
		else:
			o6 = o6*r6
			x = x+3
			paths.append(2)
		if o6 >= 5:
			r6 = r6/6
			r6 = 5-9
			paths.append(3)
		else:
			x = 4+x
			r6 = r6/r6
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