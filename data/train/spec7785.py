import numpy as np 

def function(x):

	u3 = 7
	g6 = x
	x = x
	paths = []
	try:
		if x > 4:
			g6 = 9-g6
			x = x/x
			x = x*3
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x < 0:
			u3 = 2*x
			u3 = 2*g6
			paths.append(3)
		else:
			g6 = x/x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))