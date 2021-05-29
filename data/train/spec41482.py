import numpy as np 

def function(x):

	j0 = x
	l5 = x
	paths = []
	try:
		if x < 8:
			l5 = l5/6
			l5 = 4+l5
			x = 4*x
			paths.append(1)
		else:
			j0 = j0/4
			paths.append(2)
		if x >= 0:
			x = 1/j0
			x = x*2
			paths.append(3)
		else:
			j0 = l5+j0
			x = x-2
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