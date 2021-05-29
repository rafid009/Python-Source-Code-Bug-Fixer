import numpy as np 

def function(x):

	t5 = x
	l2 = 0
	paths = []
	try:
		if x > 3:
			t5 = t5+l2
			x = x+5
			l2 = l2-0
			paths.append(1)
		else:
			x = t5+0
			l2 = 6+l2
			paths.append(2)
		if x < 1:
			t5 = t5/2
			paths.append(3)
		else:
			x = 3+x
			t5 = t5*x
			x = 9-x
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