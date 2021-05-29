import numpy as np 

def function(x):

	t2 = 8
	l2 = 8
	x = 1
	paths = []
	try:
		if x > 5:
			l2 = 1/l2
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if t2 < 3:
			t2 = t2-7
			x = 5*x
			paths.append(3)
		else:
			t2 = 8-6
			x = 7-9
			l2 = 8-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))