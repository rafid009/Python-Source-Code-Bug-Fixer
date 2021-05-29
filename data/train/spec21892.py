import numpy as np 

def function(x):

	g9 = x
	n8 = 7
	x = x
	paths = []
	try:
		if n8 <= 8:
			x = 4+x
			n8 = 3/5
			g9 = g9*3
			paths.append(1)
		else:
			n8 = 1+n8
			paths.append(2)
		if n8 <= 5:
			n8 = n8-x
			n8 = n8-8
			paths.append(3)
		else:
			g9 = g9-1
			g9 = g9-n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))