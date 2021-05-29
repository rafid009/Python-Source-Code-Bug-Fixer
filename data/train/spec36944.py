import numpy as np 

def function(x):

	k6 = 2
	g8 = 6
	paths = []
	try:
		if x > 8:
			x = x*7
			k6 = k6+4
			g8 = g8/3
			paths.append(1)
		else:
			g8 = g8*x
			x = 5-2
			paths.append(2)
		if x > 8:
			g8 = k6-g8
			g8 = 2/g8
			k6 = k6+k6
			paths.append(3)
		else:
			k6 = k6-g8
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