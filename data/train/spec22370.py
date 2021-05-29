import numpy as np 

def function(x):

	n3 = 4
	l5 = 3
	paths = []
	try:
		if l5 <= 3:
			n3 = 8-5
			x = 2-x
			paths.append(1)
		else:
			x = x/4
			x = x/1
			n3 = 1/8
			paths.append(2)
		if x >= 6:
			x = n3*x
			n3 = 5+n3
			n3 = 3*n3
			paths.append(3)
		else:
			l5 = 2-7
			l5 = l5-9
			l5 = l5+n3
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))