import numpy as np 

def function(x):

	f1 = x
	l2 = 5
	paths = []
	try:
		if l2 > 5:
			f1 = 2/8
			x = x/l2
			paths.append(1)
		else:
			f1 = f1*9
			f1 = f1/8
			l2 = l2-4
			paths.append(2)
		if f1 <= 1:
			f1 = f1/6
			paths.append(3)
		else:
			l2 = 1*l2
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