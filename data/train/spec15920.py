import numpy as np 

def function(x):

	v1 = x
	y6 = x
	x = 6
	paths = []
	try:
		if y6 <= 0:
			v1 = v1-5
			paths.append(1)
		else:
			x = 5/7
			y6 = y6+v1
			paths.append(2)
		if x <= 3:
			v1 = y6+v1
			x = 5-x
			paths.append(3)
		else:
			x = 5*3
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		v1 = y6**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))