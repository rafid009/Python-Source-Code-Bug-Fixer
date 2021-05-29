import numpy as np 

def function(x):

	l1 = 9
	b0 = x
	paths = []
	try:
		if l1 <= 2:
			b0 = x*l1
			l1 = 9-x
			x = 3/l1
			paths.append(1)
		else:
			l1 = l1-6
			paths.append(2)
		if x < 6:
			l1 = b0+l1
			b0 = b0*x
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))