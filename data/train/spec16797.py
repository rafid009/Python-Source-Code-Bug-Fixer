import numpy as np 

def function(x):

	n9 = x
	i8 = 2
	paths = []
	try:
		if n9 <= 7:
			n9 = i8+n9
			i8 = x+i8
			x = 7-n9
			paths.append(1)
		else:
			n9 = 8+n9
			x = 9*x
			n9 = n9*3
			paths.append(2)
		if n9 >= 8:
			i8 = 3/i8
			n9 = n9+n9
			paths.append(3)
		else:
			i8 = i8+i8
			x = x-5
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		n9 = i8**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))