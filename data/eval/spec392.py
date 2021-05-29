import numpy as np 

def function(x):

	l6 = x
	l4 = 2
	paths = []
	try:
		if l6 < 2:
			x = x-l6
			l4 = l4+7
			l4 = 7*l6
			paths.append(1)
		else:
			l4 = 1*l4
			l4 = l4*l6
			x = x/4
			paths.append(2)
		if l6 > 7:
			l6 = l6*x
			x = 9/5
			l6 = x-7
			paths.append(3)
		else:
			l4 = l4/4
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