import numpy as np 

def function(x):

	u2 = x
	g5 = 5
	paths = []
	try:
		if g5 < 4:
			u2 = u2*9
			x = 6+x
			u2 = u2/3
			paths.append(1)
		else:
			g5 = 3+g5
			u2 = u2+4
			u2 = x*2
			paths.append(2)
		if g5 < 2:
			x = x+1
			x = x+6
			paths.append(3)
		else:
			g5 = g5+x
			x = 4/x
			x = x-u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		g5 = u2**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))