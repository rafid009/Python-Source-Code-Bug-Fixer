import numpy as np 

def function(x):

	d9 = 1
	l2 = 2
	paths = []
	try:
		if l2 <= 4:
			x = x-7
			d9 = d9+4
			paths.append(1)
		else:
			d9 = d9*5
			paths.append(2)
		if x > 3:
			l2 = l2+l2
			l2 = l2-4
			paths.append(3)
		else:
			l2 = l2-x
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