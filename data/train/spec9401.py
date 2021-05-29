import numpy as np 

def function(x):

	k1 = x
	g0 = 1
	paths = []
	try:
		if k1 <= 0:
			g0 = g0/3
			g0 = g0/6
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x <= 3:
			k1 = k1/1
			paths.append(3)
		else:
			k1 = k1/7
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))