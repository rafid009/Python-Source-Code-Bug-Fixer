import numpy as np 

def function(x):

	e6 = x
	i8 = 9
	x = x
	paths = []
	try:
		if e6 < 7:
			i8 = i8/e6
			paths.append(1)
		else:
			i8 = i8+e6
			paths.append(2)
		if e6 >= 2:
			i8 = i8+6
			x = x*5
			e6 = e6*3
			paths.append(3)
		else:
			i8 = i8+6
			e6 = e6/8
			e6 = 8+0
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))