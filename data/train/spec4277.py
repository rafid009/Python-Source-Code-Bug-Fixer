import numpy as np 

def function(x):

	l0 = 5
	y2 = x
	paths = []
	try:
		if x > 4:
			l0 = x/l0
			paths.append(1)
		else:
			l0 = l0/x
			paths.append(2)
		if y2 < 3:
			l0 = l0/7
			paths.append(3)
		else:
			l0 = y2/4
			x = y2*8
			l0 = l0+y2
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))