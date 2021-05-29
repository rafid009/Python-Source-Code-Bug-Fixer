import numpy as np 

def function(x):

	l7 = 0
	b6 = x
	x = 3
	paths = []
	try:
		if b6 >= 3:
			x = x*x
			x = x/9
			x = 2/x
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if b6 >= 5:
			x = 1/4
			x = b6/3
			paths.append(3)
		else:
			x = 2*l7
			l7 = l7-x
			l7 = x+b6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		l7 = b6**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))