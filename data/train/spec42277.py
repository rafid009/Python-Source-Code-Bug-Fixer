import numpy as np 

def function(x):

	a2 = 8
	l6 = x
	paths = []
	try:
		if l6 > 1:
			x = x/a2
			paths.append(1)
		else:
			l6 = a2*l6
			paths.append(2)
		if x <= 4:
			x = 3-x
			paths.append(3)
		else:
			l6 = 8/l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		a2 = l6**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))