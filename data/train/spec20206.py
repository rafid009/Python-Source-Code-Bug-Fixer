import numpy as np 

def function(x):

	x4 = 3
	k6 = 1
	paths = []
	try:
		if k6 >= 1:
			k6 = k6+x4
			k6 = 5/6
			paths.append(1)
		else:
			k6 = x4+8
			paths.append(2)
		if x4 >= 7:
			x4 = x4+k6
			k6 = k6/5
			paths.append(3)
		else:
			k6 = 8-8
			x = 6-x
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