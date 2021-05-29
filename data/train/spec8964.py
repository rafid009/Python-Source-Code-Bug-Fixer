import numpy as np 

def function(x):

	v1 = x
	v4 = x
	paths = []
	try:
		if v1 < 2:
			v1 = v1+3
			v4 = v4+v4
			x = 6*x
			paths.append(1)
		else:
			x = 8/4
			v1 = v1*6
			x = v4*3
			paths.append(2)
		if v1 >= 4:
			x = 3-x
			x = 4+8
			v1 = v4-5
			paths.append(3)
		else:
			v1 = 3-9
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))