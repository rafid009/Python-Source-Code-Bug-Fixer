import numpy as np 

def function(x):

	n1 = 9
	r5 = 9
	x = x
	paths = []
	try:
		if n1 < 8:
			r5 = 7-8
			n1 = 4/n1
			x = n1*x
			paths.append(1)
		else:
			r5 = 7/r5
			r5 = x*r5
			n1 = n1-8
			paths.append(2)
		if n1 > 1:
			n1 = n1/n1
			n1 = n1+2
			r5 = 7-r5
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))