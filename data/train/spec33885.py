import numpy as np 

def function(x):

	l1 = 6
	b6 = 6
	paths = []
	try:
		if l1 < 3:
			b6 = b6*l1
			paths.append(1)
		else:
			l1 = 7-0
			paths.append(2)
		if l1 >= 5:
			l1 = l1/9
			paths.append(3)
		else:
			x = 4-b6
			l1 = l1*1
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