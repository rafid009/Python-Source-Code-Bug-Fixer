import numpy as np 

def function(x):

	l6 = x
	h5 = x
	paths = []
	try:
		if l6 > 0:
			h5 = h5+5
			l6 = l6/5
			paths.append(1)
		else:
			h5 = 9/h5
			h5 = 3+h5
			paths.append(2)
		if l6 >= 7:
			l6 = 1*l6
			paths.append(3)
		else:
			l6 = 5*l6
			l6 = x+7
			l6 = 2/l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))