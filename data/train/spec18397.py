import numpy as np 

def function(x):

	t6 = x
	l6 = 0
	paths = []
	try:
		if l6 < 8:
			l6 = l6-6
			l6 = l6/l6
			t6 = 3-t6
			paths.append(1)
		else:
			t6 = 0*t6
			paths.append(2)
		if l6 < 8:
			x = x-t6
			x = x+7
			t6 = 0/5
			paths.append(3)
		else:
			t6 = 7/1
			x = 1*x
			x = 3*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))