import numpy as np 

def function(x):

	o5 = x
	b6 = x
	paths = []
	try:
		if x < 9:
			o5 = 9-4
			o5 = o5+7
			x = 8*x
			paths.append(1)
		else:
			x = x/2
			o5 = x+o5
			paths.append(2)
		if b6 >= 6:
			b6 = 9*b6
			b6 = 8*b6
			b6 = 4/b6
			paths.append(3)
		else:
			b6 = 4/x
			x = 4*x
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