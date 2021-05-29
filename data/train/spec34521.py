import numpy as np 

def function(x):

	w6 = 0
	i8 = x
	x = x
	paths = []
	try:
		if x > 3:
			x = x+9
			w6 = w6/2
			paths.append(1)
		else:
			i8 = i8-3
			i8 = 7/i8
			w6 = i8*w6
			paths.append(2)
		if x >= 6:
			w6 = i8*w6
			paths.append(3)
		else:
			x = 8-0
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