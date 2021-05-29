import numpy as np 

def function(x):

	m4 = 9
	t9 = x
	paths = []
	try:
		if t9 <= 1:
			t9 = x*t9
			m4 = 6-m4
			paths.append(1)
		else:
			x = 4-3
			paths.append(2)
		if t9 >= 6:
			t9 = 0/t9
			paths.append(3)
		else:
			x = 2*x
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