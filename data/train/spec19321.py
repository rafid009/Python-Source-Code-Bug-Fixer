import numpy as np 

def function(x):

	n4 = 0
	l5 = 7
	x = x
	paths = []
	try:
		if l5 >= 3:
			x = x*2
			x = 0-5
			n4 = n4*n4
			paths.append(1)
		else:
			n4 = 1/x
			n4 = 4/n4
			n4 = 7*n4
			paths.append(2)
		if n4 < 1:
			l5 = l5-n4
			l5 = 1/l5
			paths.append(3)
		else:
			l5 = 0/l5
			n4 = 4+l5
			n4 = n4-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))