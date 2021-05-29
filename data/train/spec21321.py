import numpy as np 

def function(x):

	i8 = 5
	n3 = 9
	paths = []
	try:
		if n3 >= 7:
			i8 = 5*i8
			i8 = 0+i8
			paths.append(1)
		else:
			x = 8*4
			paths.append(2)
		if n3 < 9:
			n3 = n3-2
			paths.append(3)
		else:
			i8 = 2-i8
			n3 = n3+i8
			i8 = n3+i8
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		i8 = n3**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))