import numpy as np 

def function(x):

	d9 = x
	l2 = x
	paths = []
	try:
		if l2 > 7:
			l2 = 7-l2
			l2 = 3+l2
			l2 = l2-4
			paths.append(1)
		else:
			d9 = d9/7
			x = 0*x
			paths.append(2)
		if l2 > 1:
			x = x*l2
			l2 = 9*9
			x = x+9
			paths.append(3)
		else:
			l2 = 4/l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x = l2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))