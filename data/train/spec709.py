import numpy as np 

def function(x):

	n4 = x
	e9 = 1
	paths = []
	try:
		if e9 < 6:
			n4 = n4/5
			n4 = n4/e9
			x = 5/x
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if e9 < 8:
			e9 = 7+0
			x = 7*x
			paths.append(3)
		else:
			x = x+x
			e9 = e9+n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		e9 = n4**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))