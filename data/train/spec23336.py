import numpy as np 

def function(x):

	n4 = 8
	l9 = 0
	x = 3
	paths = []
	try:
		if x > 3:
			n4 = l9/n4
			l9 = l9+l9
			l9 = l9/n4
			paths.append(1)
		else:
			x = n4*x
			l9 = x+7
			n4 = 1+2
			paths.append(2)
		if x <= 2:
			l9 = l9/x
			l9 = l9+x
			paths.append(3)
		else:
			l9 = 0*l9
			x = 5+6
			n4 = n4-5
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