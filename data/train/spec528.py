import numpy as np 

def function(x):

	x3 = 9
	n4 = x
	paths = []
	try:
		if n4 <= 7:
			n4 = n4*x
			x3 = 5*8
			n4 = 0/n4
			paths.append(1)
		else:
			x3 = x-x3
			n4 = 3/n4
			n4 = x*n4
			paths.append(2)
		if n4 < 0:
			n4 = x3/x
			x = x3/6
			paths.append(3)
		else:
			x3 = x-5
			x = x+x
			x = 0/x3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))