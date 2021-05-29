import numpy as np 

def function(x):

	n7 = 9
	i8 = 4
	paths = []
	try:
		if i8 < 1:
			n7 = 1-n7
			paths.append(1)
		else:
			n7 = 7-n7
			i8 = i8-0
			paths.append(2)
		if x <= 0:
			i8 = i8+9
			x = 3*x
			i8 = 9+0
			paths.append(3)
		else:
			n7 = n7/7
			i8 = x/4
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		i8 = n7**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))