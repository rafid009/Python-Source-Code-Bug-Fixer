import numpy as np 

def function(x):

	v4 = x
	i9 = x
	paths = []
	try:
		if v4 > 7:
			x = x-7
			x = x*6
			v4 = i9-v4
			paths.append(1)
		else:
			x = 3*v4
			paths.append(2)
		if v4 < 1:
			x = 2-x
			x = x+6
			paths.append(3)
		else:
			i9 = 3*5
			x = x-v4
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))