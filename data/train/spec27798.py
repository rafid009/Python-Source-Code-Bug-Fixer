import numpy as np 

def function(x):

	i9 = 5
	g1 = x
	paths = []
	try:
		if g1 <= 9:
			g1 = 8+x
			x = x-4
			x = x*5
			paths.append(1)
		else:
			x = x/9
			i9 = 4/5
			x = x*x
			paths.append(2)
		if g1 >= 3:
			g1 = 0-1
			x = i9/7
			x = 5/i9
			paths.append(3)
		else:
			i9 = 0/i9
			i9 = i9+6
			g1 = g1/4
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))