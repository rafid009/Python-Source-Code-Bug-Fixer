import numpy as np 

def function(x):

	l1 = 3
	t9 = x
	paths = []
	try:
		if t9 < 0:
			x = 0-x
			t9 = t9/l1
			t9 = t9*l1
			paths.append(1)
		else:
			l1 = l1/5
			l1 = 5-l1
			paths.append(2)
		if x < 1:
			x = 7-x
			l1 = 9+2
			paths.append(3)
		else:
			x = x+6
			l1 = 6+t9
			t9 = 9-t9
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))