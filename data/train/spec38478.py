import numpy as np 

def function(x):

	i9 = 4
	i0 = 9
	paths = []
	try:
		if i0 > 3:
			i0 = 9+i0
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x >= 7:
			i0 = i0-6
			paths.append(3)
		else:
			i0 = i0+2
			i9 = x-0
			i9 = i9/7
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))