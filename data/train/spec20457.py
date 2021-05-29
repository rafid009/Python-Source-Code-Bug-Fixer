import numpy as np 

def function(x):

	n9 = x
	r1 = x
	paths = []
	try:
		if n9 > 3:
			n9 = n9*x
			paths.append(1)
		else:
			n9 = 6/n9
			n9 = n9/n9
			x = x-7
			paths.append(2)
		if r1 >= 5:
			n9 = 5/n9
			paths.append(3)
		else:
			n9 = r1/3
			n9 = 1/n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))