import numpy as np 

def function(x):

	d6 = x
	i8 = 4
	paths = []
	try:
		if d6 >= 4:
			x = 5*x
			paths.append(1)
		else:
			i8 = i8/x
			i8 = 9*i8
			i8 = i8*2
			paths.append(2)
		if d6 <= 3:
			x = i8-5
			x = 0+d6
			paths.append(3)
		else:
			i8 = i8/d6
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