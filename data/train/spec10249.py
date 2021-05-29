import numpy as np 

def function(x):

	t3 = 1
	l0 = x
	paths = []
	try:
		if x > 2:
			x = x-t3
			x = 3+t3
			l0 = l0/4
			paths.append(1)
		else:
			t3 = 4/3
			l0 = t3-7
			x = t3-x
			paths.append(2)
		if l0 < 1:
			l0 = 5*l0
			paths.append(3)
		else:
			x = x-x
			l0 = l0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))