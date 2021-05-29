import numpy as np 

def function(x):

	i3 = 1
	v0 = 9
	paths = []
	try:
		if x <= 3:
			v0 = 7*v0
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if x <= 3:
			v0 = v0/9
			paths.append(3)
		else:
			x = v0+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))