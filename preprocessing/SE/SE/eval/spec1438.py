import numpy as np 

def function(x):

	n9 = x
	b3 = 1
	paths = []
	try:
		if b3 < 6:
			n9 = 8*n9
			b3 = x-b3
			n9 = n9-x
			paths.append(1)
		else:
			n9 = n9-4
			x = 3*x
			b3 = n9*b3
			paths.append(2)
		if n9 <= 5:
			x = 6*b3
			x = x+7
			x = n9-x
			paths.append(3)
		else:
			n9 = x-x
			n9 = n9/5
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))