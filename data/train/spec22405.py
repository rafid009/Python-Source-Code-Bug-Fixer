import numpy as np 

def function(x):

	l5 = x
	t9 = 5
	paths = []
	try:
		if x >= 4:
			t9 = 4-t9
			x = x/1
			l5 = 6+3
			paths.append(1)
		else:
			l5 = x/l5
			paths.append(2)
		if x > 6:
			t9 = 5*t9
			x = 9*x
			paths.append(3)
		else:
			l5 = 1/l5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))