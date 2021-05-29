import numpy as np 

def function(x):

	g5 = 2
	k2 = x
	paths = []
	try:
		if x > 8:
			k2 = x*g5
			k2 = k2+3
			paths.append(1)
		else:
			x = g5+2
			paths.append(2)
		if g5 <= 3:
			g5 = 9-g5
			g5 = 4-1
			paths.append(3)
		else:
			x = x/4
			x = x*8
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))