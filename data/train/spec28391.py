import numpy as np 

def function(x):

	n9 = 3
	g9 = 1
	paths = []
	try:
		if n9 < 5:
			n9 = n9*x
			n9 = 0+n9
			x = x-4
			paths.append(1)
		else:
			n9 = 5-n9
			n9 = x-n9
			paths.append(2)
		if x >= 5:
			g9 = g9*4
			x = 5*6
			paths.append(3)
		else:
			x = x*x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))