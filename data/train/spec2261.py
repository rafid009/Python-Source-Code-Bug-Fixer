import numpy as np 

def function(x):

	w4 = 8
	l7 = 5
	paths = []
	try:
		if x < 6:
			x = x+x
			l7 = l7-x
			x = x+2
			paths.append(1)
		else:
			w4 = w4+6
			l7 = 3+1
			paths.append(2)
		if x > 6:
			x = x/2
			x = w4/x
			paths.append(3)
		else:
			w4 = w4+3
			l7 = 4*7
			x = w4/x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		w4 = l7**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))