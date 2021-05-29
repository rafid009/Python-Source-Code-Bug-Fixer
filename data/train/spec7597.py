import numpy as np 

def function(x):

	i8 = 9
	e9 = x
	paths = []
	try:
		if i8 >= 5:
			x = x+1
			paths.append(1)
		else:
			e9 = x/5
			paths.append(2)
		if e9 >= 2:
			e9 = 4-i8
			paths.append(3)
		else:
			i8 = 8+i8
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