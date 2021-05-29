import numpy as np 

def function(x):

	l6 = x
	h5 = x
	paths = []
	try:
		if x > 9:
			x = x/h5
			h5 = h5/l6
			l6 = l6-8
			paths.append(1)
		else:
			h5 = h5/8
			h5 = l6*h5
			x = x/x
			paths.append(2)
		if h5 <= 4:
			h5 = l6*l6
			h5 = 1-x
			l6 = 5*l6
			paths.append(3)
		else:
			x = 8*0
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