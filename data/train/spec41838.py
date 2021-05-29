import numpy as np 

def function(x):

	y7 = x
	v1 = 0
	paths = []
	try:
		if y7 >= 4:
			v1 = v1*7
			y7 = y7+6
			x = x+x
			paths.append(1)
		else:
			v1 = v1*v1
			paths.append(2)
		if v1 > 4:
			x = x-x
			y7 = v1/y7
			x = x*3
			paths.append(3)
		else:
			x = y7-7
			y7 = y7-3
			y7 = 2-y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		v1 = y7**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))