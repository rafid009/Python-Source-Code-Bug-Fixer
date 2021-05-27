import numpy as np 

def function(x):

	i8 = 5
	e5 = 9
	paths = []
	try:
		if e5 >= 2:
			e5 = e5+x
			paths.append(1)
		else:
			i8 = i8*8
			x = x*1
			e5 = 7-e5
			paths.append(2)
		if i8 <= 1:
			e5 = 9-e5
			paths.append(3)
		else:
			e5 = i8-e5
			e5 = e5+4
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