import numpy as np 

def function(x):

	t1 = x
	l2 = 8
	paths = []
	try:
		if t1 <= 2:
			l2 = l2/4
			paths.append(1)
		else:
			l2 = 2*l2
			paths.append(2)
		if x > 4:
			x = 1/t1
			paths.append(3)
		else:
			x = x*8
			x = x*5
			t1 = 7+t1
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