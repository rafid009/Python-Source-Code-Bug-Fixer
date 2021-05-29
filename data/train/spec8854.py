import numpy as np 

def function(x):

	i9 = 1
	v5 = x
	paths = []
	try:
		if i9 < 0:
			v5 = i9+8
			i9 = i9-v5
			i9 = i9*i9
			paths.append(1)
		else:
			v5 = i9/v5
			v5 = v5-x
			paths.append(2)
		if i9 >= 6:
			v5 = 4-6
			x = v5*1
			x = 3+x
			paths.append(3)
		else:
			i9 = x-i9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))