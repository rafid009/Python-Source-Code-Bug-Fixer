import numpy as np 

def function(x):

	n5 = x
	u0 = 9
	paths = []
	try:
		if n5 >= 5:
			x = x+6
			u0 = u0*7
			paths.append(1)
		else:
			u0 = u0*u0
			x = 9*n5
			u0 = u0+0
			paths.append(2)
		if x <= 2:
			x = n5*x
			x = 4/x
			paths.append(3)
		else:
			u0 = u0/8
			n5 = x*1
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))