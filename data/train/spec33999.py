import numpy as np 

def function(x):

	x5 = 9
	l1 = x
	paths = []
	try:
		if x5 > 0:
			x = x-l1
			x = l1/4
			paths.append(1)
		else:
			x5 = 9/9
			l1 = x5-1
			l1 = x/4
			paths.append(2)
		if x5 >= 4:
			x5 = 3*8
			x5 = x5-5
			paths.append(3)
		else:
			l1 = 7-1
			x = x+l1
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