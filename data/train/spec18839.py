import numpy as np 

def function(x):

	n4 = 9
	e9 = 0
	paths = []
	try:
		if n4 < 5:
			e9 = e9-n4
			e9 = 6-3
			paths.append(1)
		else:
			e9 = x*2
			n4 = 5*0
			n4 = x*4
			paths.append(2)
		if n4 >= 2:
			x = x/2
			e9 = 1*4
			paths.append(3)
		else:
			x = e9*x
			n4 = 4+n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))