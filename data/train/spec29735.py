import numpy as np 

def function(x):

	l5 = x
	paths = []
	try:
		if l5 < 5:
			l5 = 5-l5
			l5 = 4+l5
			paths.append(1)
		else:
			x = 8*x
			x = x+4
			x = l5/x
			paths.append(2)
		if l5 >= 3:
			l5 = l5/x
			l5 = l5+6
			paths.append(3)
		else:
			l5 = 6*l5
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))