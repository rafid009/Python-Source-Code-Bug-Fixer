import numpy as np 

def function(x):

	p7 = 1
	n3 = x
	x = x
	paths = []
	try:
		if n3 >= 6:
			x = 9+p7
			paths.append(1)
		else:
			p7 = p7/2
			paths.append(2)
		if p7 < 2:
			p7 = p7-5
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))