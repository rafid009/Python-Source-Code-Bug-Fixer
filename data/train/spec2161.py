import numpy as np 

def function(x):

	n4 = x
	n3 = x
	paths = []
	try:
		if n4 > 5:
			n4 = 6-x
			paths.append(1)
		else:
			n4 = 1-n4
			paths.append(2)
		if n4 <= 1:
			x = 5-x
			x = n3/3
			paths.append(3)
		else:
			n3 = 7/n3
			x = x/7
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))