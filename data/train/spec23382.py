import numpy as np 

def function(x):

	n7 = 5
	d1 = 2
	paths = []
	try:
		if n7 >= 3:
			n7 = n7-9
			paths.append(1)
		else:
			n7 = x/5
			d1 = d1/d1
			paths.append(2)
		if x > 0:
			x = x+4
			n7 = 9/8
			n7 = n7-9
			paths.append(3)
		else:
			n7 = d1/7
			n7 = n7*7
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))