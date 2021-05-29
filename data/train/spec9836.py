import numpy as np 

def function(x):

	g7 = 9
	q9 = x
	paths = []
	try:
		if x < 4:
			x = x-0
			g7 = 6-g7
			x = x-4
			paths.append(1)
		else:
			x = 2*x
			x = x/2
			paths.append(2)
		if x < 8:
			x = x*4
			g7 = g7/q9
			paths.append(3)
		else:
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))