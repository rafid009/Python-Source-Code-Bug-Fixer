import numpy as np 

def function(x):

	u3 = x
	g1 = 4
	paths = []
	try:
		if u3 <= 3:
			u3 = u3*6
			paths.append(1)
		else:
			u3 = 3+u3
			paths.append(2)
		if g1 >= 2:
			g1 = g1*8
			g1 = g1-g1
			x = g1-x
			paths.append(3)
		else:
			u3 = 4/9
			x = x-4
			u3 = x/u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		g1 = u3**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))