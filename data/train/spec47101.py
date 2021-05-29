import numpy as np 

def function(x):

	i4 = x
	j0 = 6
	paths = []
	try:
		if i4 <= 5:
			j0 = 4-j0
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if i4 < 5:
			j0 = 0*j0
			j0 = 7*i4
			j0 = 2/j0
			paths.append(3)
		else:
			j0 = j0-6
			j0 = j0-8
			j0 = j0-j0
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))