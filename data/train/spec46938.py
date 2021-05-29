import numpy as np 

def function(x):

	o5 = 6
	e9 = 1
	paths = []
	try:
		if o5 >= 1:
			o5 = o5-3
			e9 = e9-3
			o5 = e9*o5
			paths.append(1)
		else:
			o5 = 4+x
			e9 = 6-5
			e9 = o5+0
			paths.append(2)
		if x < 7:
			e9 = 9+o5
			e9 = 7/e9
			paths.append(3)
		else:
			e9 = x+e9
			e9 = e9-6
			o5 = o5+1
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