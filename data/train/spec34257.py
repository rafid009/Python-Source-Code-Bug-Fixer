import numpy as np 

def function(x):

	l2 = x
	d1 = 2
	paths = []
	try:
		if x <= 8:
			d1 = x-l2
			l2 = 8/l2
			paths.append(1)
		else:
			d1 = 3*d1
			d1 = d1+d1
			x = x+x
			paths.append(2)
		if d1 <= 9:
			x = x+x
			paths.append(3)
		else:
			x = d1+l2
			l2 = l2*9
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		d1 = l2**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))