import numpy as np 

def function(x):

	a9 = x
	l2 = x
	x = 8
	paths = []
	try:
		if l2 < 1:
			x = x-8
			paths.append(1)
		else:
			x = 2+7
			a9 = a9*1
			a9 = 8/a9
			paths.append(2)
		if l2 <= 2:
			x = 4*x
			paths.append(3)
		else:
			a9 = a9+a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		l2 = a9**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))