import numpy as np 

def function(x):

	e7 = 1
	v7 = 0
	paths = []
	try:
		if e7 >= 5:
			e7 = e7-x
			e7 = 6+e7
			e7 = 2/7
			paths.append(1)
		else:
			v7 = v7+x
			paths.append(2)
		if x > 7:
			x = 4+x
			paths.append(3)
		else:
			v7 = v7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))