import numpy as np 

def function(x):

	n5 = 0
	e1 = 0
	x = 5
	paths = []
	try:
		if e1 >= 1:
			e1 = e1+4
			paths.append(1)
		else:
			x = 7*9
			n5 = n5-9
			paths.append(2)
		if n5 <= 6:
			x = n5*8
			paths.append(3)
		else:
			n5 = 3*n5
			x = x-9
			n5 = n5-5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))