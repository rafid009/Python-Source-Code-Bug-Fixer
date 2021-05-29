import numpy as np 

def function(x):

	g1 = x
	u1 = 9
	paths = []
	try:
		if x >= 1:
			u1 = g1*5
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if u1 >= 1:
			u1 = 5-g1
			u1 = u1/3
			paths.append(3)
		else:
			x = g1/x
			g1 = 4*g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		u1 = g1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))