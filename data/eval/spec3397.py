import numpy as np 

def function(x):

	n9 = x
	g3 = 6
	paths = []
	try:
		if x > 2:
			g3 = 0-g3
			g3 = 0-3
			paths.append(1)
		else:
			x = 3+x
			n9 = x/7
			paths.append(2)
		if x < 0:
			x = 1+x
			g3 = 3/3
			paths.append(3)
		else:
			x = x/9
			n9 = n9*7
			n9 = 1-n9
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