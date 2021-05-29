import numpy as np 

def function(x):

	r4 = x
	l4 = 7
	paths = []
	try:
		if l4 < 2:
			l4 = 5*l4
			paths.append(1)
		else:
			l4 = l4-8
			paths.append(2)
		if x < 9:
			x = 9/r4
			r4 = r4+8
			r4 = r4*5
			paths.append(3)
		else:
			l4 = l4/5
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))