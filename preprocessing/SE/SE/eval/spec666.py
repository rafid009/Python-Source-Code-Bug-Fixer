import numpy as np 

def function(x):

	l2 = 1
	r4 = x
	paths = []
	try:
		if x > 6:
			l2 = l2*l2
			paths.append(1)
		else:
			l2 = 5-x
			paths.append(2)
		if r4 < 4:
			l2 = l2-r4
			paths.append(3)
		else:
			l2 = 2*l2
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		r4 = l2**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))