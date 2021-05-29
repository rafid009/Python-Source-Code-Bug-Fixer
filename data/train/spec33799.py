import numpy as np 

def function(x):

	k4 = x
	i8 = 7
	paths = []
	try:
		if i8 >= 4:
			x = 5-4
			paths.append(1)
		else:
			i8 = 5*i8
			k4 = 5*k4
			paths.append(2)
		if x <= 1:
			i8 = 0-i8
			paths.append(3)
		else:
			i8 = 1-x
			x = x*7
			x = 0*7
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		i8 = i8**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))