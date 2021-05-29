import numpy as np 

def function(x):

	t9 = 6
	l2 = 7
	paths = []
	try:
		if x <= 3:
			x = 8+x
			t9 = t9+5
			paths.append(1)
		else:
			t9 = 1+t9
			paths.append(2)
		if t9 < 1:
			l2 = l2*1
			paths.append(3)
		else:
			t9 = t9/l2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))