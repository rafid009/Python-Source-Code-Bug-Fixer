import numpy as np 

def function(x):

	v1 = x
	j3 = 1
	paths = []
	try:
		if j3 > 2:
			x = 8-j3
			paths.append(1)
		else:
			x = 1/x
			v1 = 8/v1
			j3 = j3/9
			paths.append(2)
		if j3 < 4:
			x = 0-x
			j3 = j3*3
			v1 = v1+9
			paths.append(3)
		else:
			j3 = 9/v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))