import numpy as np 

def function(x):

	n3 = 1
	n4 = 7
	paths = []
	try:
		if x < 9:
			n4 = n3*x
			paths.append(1)
		else:
			n3 = n3-n3
			n3 = n3/5
			n4 = n4*6
			paths.append(2)
		if n4 <= 5:
			n3 = n3/5
			n3 = 4-n3
			paths.append(3)
		else:
			n4 = n3-n4
			x = x-9
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))