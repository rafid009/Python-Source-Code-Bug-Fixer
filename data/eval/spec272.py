import numpy as np 

def function(x):

	t3 = x
	l7 = x
	paths = []
	try:
		if l7 >= 2:
			l7 = l7/t3
			l7 = l7-x
			l7 = 9-l7
			paths.append(1)
		else:
			t3 = 1/t3
			t3 = 0/t3
			paths.append(2)
		if l7 <= 7:
			t3 = t3-l7
			t3 = 0/t3
			l7 = 9-8
			paths.append(3)
		else:
			x = x-8
			t3 = 1/t3
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