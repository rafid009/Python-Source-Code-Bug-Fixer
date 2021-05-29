import numpy as np 

def function(x):

	n1 = 5
	l0 = x
	paths = []
	try:
		if x > 1:
			n1 = n1/9
			x = 1/n1
			x = l0/2
			paths.append(1)
		else:
			x = x/9
			n1 = 8/n1
			paths.append(2)
		if x <= 8:
			n1 = n1-1
			paths.append(3)
		else:
			l0 = 3+l0
			l0 = 4*l0
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		n1 = l0**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))