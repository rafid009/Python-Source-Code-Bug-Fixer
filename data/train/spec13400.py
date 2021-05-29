import numpy as np 

def function(x):

	b5 = 4
	l7 = 5
	paths = []
	try:
		if b5 >= 8:
			l7 = 5+9
			l7 = 8+b5
			paths.append(1)
		else:
			l7 = l7*l7
			paths.append(2)
		if b5 <= 6:
			l7 = l7-l7
			x = 1-b5
			l7 = x-9
			paths.append(3)
		else:
			l7 = b5*l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))