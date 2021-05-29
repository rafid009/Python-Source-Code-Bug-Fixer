import numpy as np 

def function(x):

	n8 = x
	g1 = x
	paths = []
	try:
		if x > 4:
			x = n8*x
			paths.append(1)
		else:
			g1 = g1/4
			paths.append(2)
		if n8 < 4:
			x = n8+x
			paths.append(3)
		else:
			g1 = x+g1
			x = x-2
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))