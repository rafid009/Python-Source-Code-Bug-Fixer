import numpy as np 

def function(x):

	i8 = 6
	i1 = x
	paths = []
	try:
		if i8 >= 7:
			i1 = i8*i8
			paths.append(1)
		else:
			i8 = 1-i8
			x = x-9
			paths.append(2)
		if i8 < 3:
			x = 3/1
			i1 = i1*8
			x = 3*8
			paths.append(3)
		else:
			x = 1-x
			i1 = 0*i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))