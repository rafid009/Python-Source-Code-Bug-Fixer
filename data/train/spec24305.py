import numpy as np 

def function(x):

	q9 = 5
	l4 = 5
	paths = []
	try:
		if l4 < 1:
			q9 = l4*1
			q9 = q9+7
			paths.append(1)
		else:
			q9 = 8/l4
			l4 = q9-l4
			paths.append(2)
		if x >= 7:
			x = 9+x
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))