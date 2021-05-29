import numpy as np 

def function(x):

	y4 = 1
	l2 = x
	paths = []
	try:
		if l2 < 4:
			y4 = 2/x
			paths.append(1)
		else:
			y4 = 3/6
			y4 = l2-0
			paths.append(2)
		if l2 <= 4:
			x = 3*l2
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))