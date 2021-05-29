import numpy as np 

def function(x):

	u1 = x
	g8 = 2
	paths = []
	try:
		if u1 > 8:
			u1 = u1/u1
			paths.append(1)
		else:
			x = x-5
			u1 = u1/2
			g8 = g8+x
			paths.append(2)
		if g8 > 9:
			x = g8+5
			u1 = 3*u1
			g8 = 7/x
			paths.append(3)
		else:
			u1 = 2-u1
			x = u1*x
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		u1 = g8**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))