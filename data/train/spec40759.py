import numpy as np 

def function(x):

	u0 = x
	g5 = 2
	paths = []
	try:
		if x >= 8:
			x = 0/3
			u0 = g5*1
			paths.append(1)
		else:
			g5 = 9/4
			paths.append(2)
		if u0 <= 8:
			x = x/1
			g5 = g5-8
			u0 = g5-g5
			paths.append(3)
		else:
			g5 = g5+9
			g5 = 2/g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))