import numpy as np 

def function(x):

	j5 = 1
	v0 = x
	paths = []
	try:
		if v0 >= 7:
			v0 = v0-4
			paths.append(1)
		else:
			x = 8*x
			paths.append(2)
		if v0 < 7:
			j5 = j5*5
			v0 = x/x
			x = x+2
			paths.append(3)
		else:
			x = j5*x
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