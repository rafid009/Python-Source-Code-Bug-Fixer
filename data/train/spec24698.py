import numpy as np 

def function(x):

	g5 = x
	u6 = x
	paths = []
	try:
		if g5 <= 2:
			u6 = u6*g5
			paths.append(1)
		else:
			g5 = g5-2
			x = x-6
			g5 = g5/x
			paths.append(2)
		if u6 <= 2:
			u6 = 4*g5
			paths.append(3)
		else:
			u6 = 7*g5
			u6 = u6+1
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		g5 = u6**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))