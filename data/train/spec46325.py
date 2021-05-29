import numpy as np 

def function(x):

	x6 = 6
	n1 = x
	paths = []
	try:
		if x6 >= 9:
			x6 = x6/x6
			x = 2/3
			paths.append(1)
		else:
			x = 5+x
			n1 = n1*6
			paths.append(2)
		if x6 < 4:
			x = x-1
			paths.append(3)
		else:
			x = n1-n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))