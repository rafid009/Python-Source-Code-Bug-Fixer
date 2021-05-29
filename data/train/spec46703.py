import numpy as np 

def function(x):

	l2 = x
	b7 = 3
	paths = []
	try:
		if x <= 0:
			l2 = 6-3
			x = 3-x
			b7 = l2/b7
			paths.append(1)
		else:
			l2 = l2-7
			b7 = b7-3
			b7 = b7*b7
			paths.append(2)
		if b7 < 7:
			x = x*b7
			l2 = l2*2
			b7 = 5-l2
			paths.append(3)
		else:
			b7 = b7/x
			x = x+4
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