import numpy as np 

def function(x):

	y4 = 6
	l2 = x
	paths = []
	try:
		if y4 > 1:
			y4 = 2+y4
			paths.append(1)
		else:
			l2 = l2*l2
			l2 = 5/l2
			paths.append(2)
		if l2 < 6:
			x = 7*9
			paths.append(3)
		else:
			x = y4+x
			l2 = 7+l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		y4 = l2**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))