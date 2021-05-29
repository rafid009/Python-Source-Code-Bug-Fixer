import numpy as np 

def function(x):

	k7 = x
	g5 = 8
	paths = []
	try:
		if x > 0:
			k7 = k7*g5
			paths.append(1)
		else:
			g5 = k7+1
			paths.append(2)
		if x > 7:
			x = x*x
			paths.append(3)
		else:
			x = g5/3
			x = 8*4
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))