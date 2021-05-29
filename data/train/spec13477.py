import numpy as np 

def function(x):

	v1 = 8
	x6 = x
	paths = []
	try:
		if v1 >= 2:
			x6 = v1/6
			paths.append(1)
		else:
			x6 = x6*x6
			paths.append(2)
		if x6 > 5:
			x6 = 4/6
			v1 = v1*1
			paths.append(3)
		else:
			v1 = 6*x
			x6 = 1-x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		v1 = x6**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))