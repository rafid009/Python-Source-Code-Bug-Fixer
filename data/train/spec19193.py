import numpy as np 

def function(x):

	k6 = x
	g0 = x
	paths = []
	try:
		if k6 <= 0:
			k6 = x+k6
			k6 = k6/5
			g0 = g0+6
			paths.append(1)
		else:
			x = 4/x
			paths.append(2)
		if k6 > 8:
			g0 = 6/1
			paths.append(3)
		else:
			k6 = k6*7
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