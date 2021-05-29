import numpy as np 

def function(x):

	g4 = 4
	u1 = 8
	x = x
	paths = []
	try:
		if u1 > 9:
			x = u1+8
			u1 = 2+1
			paths.append(1)
		else:
			u1 = g4-g4
			paths.append(2)
		if x > 0:
			u1 = g4+u1
			paths.append(3)
		else:
			u1 = u1*g4
			g4 = g4/g4
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