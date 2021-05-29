import numpy as np 

def function(x):

	y1 = x
	l6 = 1
	paths = []
	try:
		if l6 < 3:
			l6 = l6-x
			paths.append(1)
		else:
			x = l6+6
			l6 = 5/5
			paths.append(2)
		if l6 < 2:
			l6 = y1/x
			x = y1+x
			paths.append(3)
		else:
			l6 = y1/l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))