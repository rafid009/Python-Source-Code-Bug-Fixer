import numpy as np 

def function(x):

	l7 = x
	n8 = 2
	paths = []
	try:
		if n8 > 8:
			x = 2*x
			x = x/2
			paths.append(1)
		else:
			n8 = n8-6
			paths.append(2)
		if l7 <= 5:
			l7 = 5+l7
			l7 = 9+l7
			paths.append(3)
		else:
			n8 = 5+n8
			l7 = l7+l7
			l7 = 6-l7
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))