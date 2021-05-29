import numpy as np 

def function(x):

	k2 = 6
	g3 = 2
	paths = []
	try:
		if k2 > 7:
			g3 = x/7
			g3 = 5+g3
			paths.append(1)
		else:
			k2 = 3*x
			g3 = 1*g3
			paths.append(2)
		if x < 0:
			k2 = x-1
			x = x+7
			paths.append(3)
		else:
			g3 = 0+x
			g3 = 3+g3
			k2 = 1/k2
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