import numpy as np 

def function(x):

	v7 = 5
	i7 = 2
	paths = []
	try:
		if x > 5:
			i7 = 5-9
			v7 = 0+v7
			x = 9/x
			paths.append(1)
		else:
			v7 = v7*i7
			paths.append(2)
		if x > 0:
			x = x/7
			x = x-1
			v7 = i7+0
			paths.append(3)
		else:
			v7 = 0-x
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))