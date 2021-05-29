import numpy as np 

def function(x):

	e2 = 3
	i7 = x
	paths = []
	try:
		if x >= 1:
			i7 = i7+0
			x = 7/6
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if i7 >= 1:
			x = x*3
			i7 = x-i7
			x = x+x
			paths.append(3)
		else:
			i7 = i7*e2
			x = x*i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))