import numpy as np 

def function(x):

	g1 = x
	u6 = x
	x = x
	paths = []
	try:
		if u6 <= 7:
			x = 4/x
			u6 = 8/8
			paths.append(1)
		else:
			g1 = g1/8
			g1 = 6+x
			paths.append(2)
		if g1 >= 9:
			x = 4/u6
			g1 = x-x
			g1 = g1-1
			paths.append(3)
		else:
			u6 = u6-6
			x = x/x
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))