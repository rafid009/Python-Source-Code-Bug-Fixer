import numpy as np 

def function(x):

	u3 = x
	g9 = 5
	paths = []
	try:
		if x >= 7:
			u3 = 0-u3
			x = g9*4
			paths.append(1)
		else:
			x = 2+x
			x = x/x
			g9 = x*u3
			paths.append(2)
		if g9 > 0:
			g9 = 8+g9
			paths.append(3)
		else:
			u3 = 1/8
			u3 = u3/4
			u3 = u3*g9
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))