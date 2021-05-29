import numpy as np 

def function(x):

	k6 = 0
	v3 = x
	paths = []
	try:
		if v3 > 7:
			k6 = k6*v3
			paths.append(1)
		else:
			v3 = 3/v3
			paths.append(2)
		if k6 <= 0:
			k6 = 3-k6
			x = x+x
			v3 = 2/v3
			paths.append(3)
		else:
			x = 7-x
			x = v3-v3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))