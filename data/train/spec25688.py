import numpy as np 

def function(x):

	u2 = x
	g9 = 5
	paths = []
	try:
		if g9 < 8:
			g9 = g9/1
			x = u2+2
			u2 = u2-g9
			paths.append(1)
		else:
			g9 = 4-2
			u2 = 0*9
			u2 = 1*6
			paths.append(2)
		if x > 5:
			g9 = g9-8
			paths.append(3)
		else:
			g9 = g9*1
			u2 = u2-g9
			u2 = 8*u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))