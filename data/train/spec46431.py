import numpy as np 

def function(x):

	g3 = x
	u1 = 4
	paths = []
	try:
		if g3 > 4:
			x = 3/x
			u1 = u1-3
			x = x+0
			paths.append(1)
		else:
			u1 = u1+u1
			paths.append(2)
		if x > 6:
			g3 = 7/g3
			paths.append(3)
		else:
			g3 = x*g3
			u1 = 7/8
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