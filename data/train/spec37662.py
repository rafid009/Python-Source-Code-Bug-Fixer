import numpy as np 

def function(x):

	l1 = 2
	b6 = 4
	paths = []
	try:
		if b6 < 5:
			l1 = l1-b6
			b6 = 6/b6
			paths.append(1)
		else:
			b6 = 2*l1
			x = x+7
			paths.append(2)
		if x > 7:
			x = 0+b6
			paths.append(3)
		else:
			x = 7/x
			x = x+x
			l1 = 8-b6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))