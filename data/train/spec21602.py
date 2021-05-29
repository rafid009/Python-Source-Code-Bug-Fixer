import numpy as np 

def function(x):

	g9 = x
	b9 = 6
	x = 1
	paths = []
	try:
		if g9 > 0:
			g9 = x*8
			g9 = g9-1
			paths.append(1)
		else:
			b9 = b9*3
			paths.append(2)
		if g9 < 8:
			b9 = b9-4
			x = 7/6
			g9 = b9-8
			paths.append(3)
		else:
			b9 = 6/b9
			x = 7*b9
			b9 = b9+b9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))