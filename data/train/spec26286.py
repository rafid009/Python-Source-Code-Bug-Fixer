import numpy as np 

def function(x):

	l1 = x
	r2 = 1
	paths = []
	try:
		if l1 <= 9:
			x = x/5
			paths.append(1)
		else:
			r2 = 3+5
			paths.append(2)
		if l1 <= 9:
			r2 = 1+r2
			r2 = 8/6
			x = x/4
			paths.append(3)
		else:
			x = 9*x
			l1 = l1*5
			r2 = 1/r2
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		r2 = l1**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))