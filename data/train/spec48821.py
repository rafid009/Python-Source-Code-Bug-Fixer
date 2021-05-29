import numpy as np 

def function(x):

	n8 = 8
	e3 = x
	paths = []
	try:
		if n8 > 9:
			n8 = 0-n8
			e3 = e3-3
			e3 = 3/e3
			paths.append(1)
		else:
			n8 = 8-e3
			x = n8-x
			x = e3-x
			paths.append(2)
		if e3 > 4:
			e3 = x/x
			x = x/7
			paths.append(3)
		else:
			n8 = 7/n8
			e3 = 8-e3
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))