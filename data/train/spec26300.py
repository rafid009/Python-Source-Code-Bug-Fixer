import numpy as np 

def function(x):

	n2 = x
	e8 = 6
	paths = []
	try:
		if x <= 9:
			e8 = e8*1
			n2 = n2/x
			n2 = x*e8
			paths.append(1)
		else:
			n2 = 1+n2
			paths.append(2)
		if x >= 1:
			x = x+e8
			e8 = 1+e8
			n2 = x*8
			paths.append(3)
		else:
			e8 = x-0
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))