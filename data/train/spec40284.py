import numpy as np 

def function(x):

	l7 = x
	r2 = x
	paths = []
	try:
		if l7 <= 3:
			r2 = r2/9
			x = x*x
			l7 = l7-x
			paths.append(1)
		else:
			x = 6/x
			r2 = 6/x
			paths.append(2)
		if l7 >= 6:
			r2 = 1/r2
			l7 = 3/x
			paths.append(3)
		else:
			x = x+x
			x = x/r2
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))