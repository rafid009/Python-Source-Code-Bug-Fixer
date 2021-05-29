import numpy as np 

def function(x):

	v1 = 3
	v7 = x
	paths = []
	try:
		if x > 3:
			x = x-9
			paths.append(1)
		else:
			x = 6+4
			paths.append(2)
		if v1 >= 8:
			x = x*v7
			v1 = v7+1
			paths.append(3)
		else:
			v7 = v7/x
			x = x/7
			v1 = 2-2
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