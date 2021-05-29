import numpy as np 

def function(x):

	n9 = 2
	l3 = 9
	paths = []
	try:
		if x < 9:
			l3 = 6/3
			paths.append(1)
		else:
			l3 = l3+6
			n9 = n9+8
			l3 = l3*x
			paths.append(2)
		if x > 2:
			x = x+l3
			x = 3+x
			paths.append(3)
		else:
			n9 = 1-2
			l3 = l3/l3
			n9 = x-6
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))