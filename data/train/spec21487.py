import numpy as np 

def function(x):

	z5 = x
	n9 = 0
	paths = []
	try:
		if n9 >= 5:
			x = x*x
			paths.append(1)
		else:
			x = 5-x
			n9 = n9+1
			paths.append(2)
		if n9 > 4:
			x = 5-0
			x = x+x
			x = 2+x
			paths.append(3)
		else:
			n9 = n9*n9
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))