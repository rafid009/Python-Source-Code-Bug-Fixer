import numpy as np 

def function(x):

	n3 = 9
	q5 = 7
	paths = []
	try:
		if n3 <= 2:
			n3 = n3*9
			paths.append(1)
		else:
			n3 = 0-n3
			paths.append(2)
		if n3 >= 1:
			x = 6-x
			paths.append(3)
		else:
			x = 4-x
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