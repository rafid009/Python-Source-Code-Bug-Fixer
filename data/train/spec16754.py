import numpy as np 

def function(x):

	l8 = 4
	t3 = x
	paths = []
	try:
		if l8 < 5:
			x = x-t3
			x = x+2
			x = x*2
			paths.append(1)
		else:
			x = x/x
			l8 = 1+l8
			x = l8/5
			paths.append(2)
		if l8 < 6:
			l8 = 1-l8
			paths.append(3)
		else:
			x = x-7
			l8 = x+4
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))