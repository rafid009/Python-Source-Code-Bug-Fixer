import numpy as np 

def function(x):

	l9 = x
	n3 = x
	paths = []
	try:
		if x > 7:
			l9 = l9-x
			paths.append(1)
		else:
			l9 = l9*8
			n3 = n3+n3
			n3 = n3-l9
			paths.append(2)
		if n3 >= 0:
			n3 = 9*n3
			n3 = n3-8
			n3 = 6/9
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))