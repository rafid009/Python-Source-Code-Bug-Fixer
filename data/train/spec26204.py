import numpy as np 

def function(x):

	l4 = 6
	n9 = x
	paths = []
	try:
		if l4 < 2:
			l4 = n9/n9
			l4 = n9*l4
			x = 8-x
			paths.append(1)
		else:
			n9 = n9-2
			n9 = n9/x
			x = x*l4
			paths.append(2)
		if l4 <= 2:
			n9 = n9+8
			x = n9*6
			x = 6-0
			paths.append(3)
		else:
			n9 = 6+6
			n9 = x*n9
			n9 = 7-n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		l4 = n9**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))