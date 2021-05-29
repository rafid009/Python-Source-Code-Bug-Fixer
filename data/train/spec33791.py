import numpy as np 

def function(x):

	u1 = 4
	g9 = x
	paths = []
	try:
		if g9 > 3:
			g9 = g9+5
			g9 = g9/8
			x = x+g9
			paths.append(1)
		else:
			g9 = 6+1
			paths.append(2)
		if g9 < 9:
			u1 = 0-u1
			paths.append(3)
		else:
			x = x/x
			g9 = 9/g9
			u1 = x/u1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))