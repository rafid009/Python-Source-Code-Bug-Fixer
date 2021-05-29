import numpy as np 

def function(x):

	t6 = x
	q6 = 4
	paths = []
	try:
		if t6 <= 2:
			q6 = q6/3
			x = x/q6
			paths.append(1)
		else:
			q6 = q6/9
			paths.append(2)
		if x >= 9:
			t6 = 9*5
			q6 = q6+0
			paths.append(3)
		else:
			q6 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))