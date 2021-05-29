import numpy as np 

def function(x):

	b8 = 0
	l2 = 6
	x = x
	paths = []
	try:
		if x > 9:
			x = x/9
			paths.append(1)
		else:
			l2 = 5/l2
			paths.append(2)
		if b8 > 4:
			l2 = l2+6
			l2 = 6-3
			paths.append(3)
		else:
			x = x+9
			l2 = 5/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))