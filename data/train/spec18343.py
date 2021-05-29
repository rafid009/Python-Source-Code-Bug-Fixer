import numpy as np 

def function(x):

	o7 = 8
	x7 = 3
	paths = []
	try:
		if x7 > 4:
			x = x/x
			x = x*x7
			paths.append(1)
		else:
			o7 = 3+x
			o7 = o7*x
			paths.append(2)
		if o7 > 5:
			x7 = x7-8
			x7 = x7/3
			paths.append(3)
		else:
			o7 = x*9
			x = x+6
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))