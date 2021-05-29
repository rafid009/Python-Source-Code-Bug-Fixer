import numpy as np 

def function(x):

	l5 = 5
	l4 = x
	paths = []
	try:
		if l5 > 9:
			l4 = 6+l4
			l5 = l5*l5
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if l5 > 0:
			x = x/l4
			paths.append(3)
		else:
			l5 = l5+5
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l5 = l4**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))