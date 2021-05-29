import numpy as np 

def function(x):

	a8 = 7
	v6 = 6
	paths = []
	try:
		if a8 <= 4:
			x = x-a8
			x = 2-x
			paths.append(1)
		else:
			a8 = 6/x
			v6 = 1+v6
			paths.append(2)
		if v6 >= 2:
			x = x/1
			paths.append(3)
		else:
			x = 0*6
			x = x+x
			a8 = a8+7
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