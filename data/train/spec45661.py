import numpy as np 

def function(x):

	i8 = x
	j0 = 4
	paths = []
	try:
		if x < 2:
			j0 = x*j0
			paths.append(1)
		else:
			x = 4-i8
			x = j0/8
			j0 = j0-x
			paths.append(2)
		if x >= 6:
			j0 = x+j0
			x = j0*j0
			i8 = i8/i8
			paths.append(3)
		else:
			x = 5+i8
			j0 = x-j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))