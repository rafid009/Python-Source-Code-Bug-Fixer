import numpy as np 

def function(x):

	z5 = 5
	i8 = x
	paths = []
	try:
		if z5 >= 9:
			i8 = i8*9
			x = x+i8
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if i8 > 7:
			i8 = z5/i8
			x = z5-z5
			paths.append(3)
		else:
			i8 = i8+1
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