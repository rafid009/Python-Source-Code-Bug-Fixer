import numpy as np 

def function(x):

	x8 = 8
	l2 = x
	x = 2
	paths = []
	try:
		if l2 < 6:
			x8 = x8/x
			x8 = x8+1
			x8 = x8-9
			paths.append(1)
		else:
			x8 = 8/l2
			l2 = 1-l2
			x = x/5
			paths.append(2)
		if l2 < 3:
			l2 = 4-x
			paths.append(3)
		else:
			l2 = 2+x8
			x = 5/x
			x8 = x8-1
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))