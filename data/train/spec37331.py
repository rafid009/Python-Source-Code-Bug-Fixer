import numpy as np 

def function(x):

	o7 = 6
	x9 = x
	paths = []
	try:
		if x <= 4:
			o7 = o7*x
			x9 = x9-x9
			paths.append(1)
		else:
			x = o7+8
			o7 = x9/x
			paths.append(2)
		if o7 <= 7:
			o7 = 5+o7
			o7 = 3+o7
			paths.append(3)
		else:
			x9 = x+x
			x9 = 7*x9
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x9 = o7**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))