import numpy as np 

def function(x):

	f0 = x
	o5 = x
	paths = []
	try:
		if f0 >= 6:
			f0 = o5-6
			paths.append(1)
		else:
			x = x+5
			f0 = f0-f0
			paths.append(2)
		if x > 1:
			x = x-x
			o5 = o5*o5
			paths.append(3)
		else:
			o5 = o5-x
			f0 = o5*5
			x = 6*f0
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))