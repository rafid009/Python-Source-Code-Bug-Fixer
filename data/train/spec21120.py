import numpy as np 

def function(x):

	l5 = 4
	l0 = x
	paths = []
	try:
		if x <= 1:
			l5 = 5-l5
			x = x/1
			l5 = 0*6
			paths.append(1)
		else:
			x = l0/x
			paths.append(2)
		if x > 0:
			l0 = 3+0
			x = 7/x
			l5 = l5+x
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))