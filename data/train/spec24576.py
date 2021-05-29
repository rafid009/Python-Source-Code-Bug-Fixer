import numpy as np 

def function(x):

	i9 = 5
	v4 = x
	paths = []
	try:
		if x >= 0:
			x = x*3
			paths.append(1)
		else:
			x = x/2
			v4 = 3+9
			x = 5-7
			paths.append(2)
		if i9 < 6:
			i9 = 1/6
			paths.append(3)
		else:
			x = x+5
			i9 = v4-i9
			x = i9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))