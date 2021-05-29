import numpy as np 

def function(x):

	n9 = x
	a7 = x
	paths = []
	try:
		if n9 >= 8:
			x = x-1
			a7 = a7/n9
			a7 = a7*5
			paths.append(1)
		else:
			a7 = n9-n9
			paths.append(2)
		if x < 6:
			a7 = 7-7
			paths.append(3)
		else:
			a7 = 1-0
			n9 = 4/n9
			n9 = n9*1
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))