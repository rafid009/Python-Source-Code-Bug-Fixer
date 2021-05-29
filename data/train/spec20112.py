import numpy as np 

def function(x):

	i9 = x
	k4 = x
	paths = []
	try:
		if i9 > 7:
			x = x-3
			paths.append(1)
		else:
			i9 = x-4
			paths.append(2)
		if x <= 9:
			i9 = 0+2
			x = 4*4
			k4 = x/k4
			paths.append(3)
		else:
			i9 = i9/k4
			i9 = 4-x
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		i9 = k4**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))