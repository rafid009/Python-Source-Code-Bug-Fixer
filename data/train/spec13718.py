import numpy as np 

def function(x):

	v7 = x
	e8 = 7
	paths = []
	try:
		if v7 >= 9:
			v7 = e8+v7
			paths.append(1)
		else:
			v7 = 5+v7
			e8 = e8*3
			paths.append(2)
		if x > 3:
			x = 9+x
			x = x+x
			paths.append(3)
		else:
			e8 = e8*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))