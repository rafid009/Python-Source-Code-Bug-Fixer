import numpy as np 

def function(x):

	x8 = 8
	l2 = x
	paths = []
	try:
		if x <= 9:
			l2 = 3/l2
			x = x8+x8
			x8 = x*l2
			paths.append(1)
		else:
			l2 = l2/8
			l2 = 3-l2
			x = x+l2
			paths.append(2)
		if l2 >= 2:
			l2 = x-4
			x = 2+3
			x8 = x8*3
			paths.append(3)
		else:
			x8 = 7-9
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x8 = l2**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))