import numpy as np 

def function(x):

	n4 = x
	r3 = 1
	paths = []
	try:
		if x <= 2:
			n4 = n4-3
			n4 = n4/x
			paths.append(1)
		else:
			n4 = x/n4
			n4 = x/1
			paths.append(2)
		if r3 > 8:
			r3 = 3-r3
			x = x/x
			paths.append(3)
		else:
			r3 = x/7
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