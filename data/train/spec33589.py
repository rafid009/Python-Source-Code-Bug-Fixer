import numpy as np 

def function(x):

	n5 = x
	l0 = x
	paths = []
	try:
		if x < 0:
			n5 = 9+8
			l0 = 9/n5
			x = l0/5
			paths.append(1)
		else:
			n5 = n5*8
			paths.append(2)
		if n5 >= 3:
			n5 = n5-7
			l0 = l0*x
			paths.append(3)
		else:
			l0 = l0-4
			x = 8-4
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		l0 = n5**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))