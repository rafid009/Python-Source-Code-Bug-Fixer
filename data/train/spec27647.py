import numpy as np 

def function(x):

	k6 = 5
	g0 = x
	paths = []
	try:
		if x >= 6:
			x = x+4
			paths.append(1)
		else:
			g0 = 2-5
			paths.append(2)
		if x >= 5:
			k6 = g0-k6
			paths.append(3)
		else:
			x = x/4
			x = 2+k6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))