import numpy as np 

def function(x):

	q6 = 3
	t9 = 0
	paths = []
	try:
		if x < 3:
			q6 = q6/q6
			paths.append(1)
		else:
			x = x/4
			t9 = 1/3
			paths.append(2)
		if t9 >= 4:
			t9 = q6/t9
			q6 = x/4
			paths.append(3)
		else:
			x = x+3
			t9 = q6*t9
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