import numpy as np 

def function(x):

	l0 = x
	l5 = 5
	paths = []
	try:
		if l5 > 0:
			l5 = l5/x
			x = x-5
			paths.append(1)
		else:
			l5 = 7/l0
			l0 = l0/l5
			paths.append(2)
		if l0 < 5:
			x = 4*5
			l0 = l0+8
			paths.append(3)
		else:
			l0 = 0-l0
			l0 = l0-6
			l5 = l5-5
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l5 = l0**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))