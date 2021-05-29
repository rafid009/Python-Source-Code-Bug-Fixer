import numpy as np 

def function(x):

	o5 = 3
	x0 = x
	paths = []
	try:
		if x0 >= 7:
			x0 = 4+5
			x = x/1
			x0 = x0-o5
			paths.append(1)
		else:
			x0 = x0*5
			o5 = 6/x0
			o5 = o5*9
			paths.append(2)
		if x0 <= 3:
			x0 = 3+8
			o5 = 6-o5
			paths.append(3)
		else:
			o5 = 8+8
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))