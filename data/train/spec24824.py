import numpy as np 

def function(x):

	l0 = 0
	q2 = x
	paths = []
	try:
		if l0 <= 6:
			x = x/2
			paths.append(1)
		else:
			q2 = q2-6
			q2 = q2-l0
			x = 3-x
			paths.append(2)
		if l0 >= 1:
			x = q2*7
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))