import numpy as np 

def function(x):

	l1 = x
	f1 = x
	x = x
	paths = []
	try:
		if l1 <= 2:
			l1 = 1*l1
			f1 = 7/f1
			l1 = x-l1
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if l1 <= 2:
			x = x*2
			f1 = f1*3
			x = 5/x
			paths.append(3)
		else:
			f1 = f1-l1
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