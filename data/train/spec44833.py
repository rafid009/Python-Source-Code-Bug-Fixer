import numpy as np 

def function(x):

	a1 = 5
	l4 = x
	paths = []
	try:
		if a1 < 5:
			l4 = x+l4
			a1 = 7+4
			paths.append(1)
		else:
			l4 = a1+l4
			x = x-a1
			paths.append(2)
		if l4 < 1:
			a1 = a1-6
			paths.append(3)
		else:
			l4 = 2/4
			a1 = 4-l4
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))