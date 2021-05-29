import numpy as np 

def function(x):

	d2 = 5
	n1 = 5
	x = x
	paths = []
	try:
		if x <= 0:
			x = 3-x
			d2 = d2*6
			n1 = 2-4
			paths.append(1)
		else:
			n1 = n1-9
			d2 = d2*n1
			paths.append(2)
		if x < 7:
			d2 = d2*3
			paths.append(3)
		else:
			n1 = 7*n1
			d2 = 5/d2
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))