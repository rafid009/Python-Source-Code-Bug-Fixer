import numpy as np 

def function(x):

	e0 = 1
	n4 = 5
	paths = []
	try:
		if e0 < 0:
			n4 = 0/n4
			paths.append(1)
		else:
			n4 = 2+1
			n4 = n4-x
			paths.append(2)
		if e0 <= 4:
			n4 = x*e0
			e0 = 2*e0
			paths.append(3)
		else:
			x = x/5
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