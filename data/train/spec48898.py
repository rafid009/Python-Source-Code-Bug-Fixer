import numpy as np 

def function(x):

	l5 = 3
	n8 = 6
	paths = []
	try:
		if x > 6:
			l5 = 8/l5
			x = x*6
			l5 = 6-l5
			paths.append(1)
		else:
			l5 = l5+l5
			paths.append(2)
		if x <= 0:
			l5 = 7/2
			l5 = 2-n8
			x = x+x
			paths.append(3)
		else:
			n8 = n8/5
			l5 = l5/1
			x = n8-3
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