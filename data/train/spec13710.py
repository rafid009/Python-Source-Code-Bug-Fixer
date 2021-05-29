import numpy as np 

def function(x):

	v4 = 1
	k6 = x
	x = 0
	paths = []
	try:
		if k6 < 9:
			v4 = 9+k6
			k6 = k6*k6
			k6 = v4/7
			paths.append(1)
		else:
			x = x/9
			x = 9/3
			k6 = k6-6
			paths.append(2)
		if x >= 3:
			x = 9*k6
			paths.append(3)
		else:
			k6 = v4-9
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))