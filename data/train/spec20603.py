import numpy as np 

def function(x):

	n5 = x
	h2 = 5
	x = 6
	paths = []
	try:
		if h2 >= 4:
			n5 = n5/h2
			paths.append(1)
		else:
			n5 = n5/6
			paths.append(2)
		if n5 > 3:
			x = 7*x
			paths.append(3)
		else:
			h2 = 8/3
			h2 = n5+n5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))