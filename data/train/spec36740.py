import numpy as np 

def function(x):

	k8 = x
	l2 = 3
	paths = []
	try:
		if x >= 3:
			x = x*x
			x = 7-x
			paths.append(1)
		else:
			l2 = 2/l2
			paths.append(2)
		if l2 >= 2:
			l2 = 0-l2
			k8 = k8*6
			paths.append(3)
		else:
			x = x/4
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