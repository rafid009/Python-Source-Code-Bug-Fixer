import numpy as np 

def function(x):

	t3 = x
	q2 = 4
	paths = []
	try:
		if x <= 0:
			t3 = 3+8
			q2 = 2/t3
			paths.append(1)
		else:
			q2 = x/t3
			x = 9/1
			paths.append(2)
		if q2 < 2:
			t3 = t3-5
			t3 = 8*t3
			x = t3/4
			paths.append(3)
		else:
			t3 = 8-8
			t3 = q2/t3
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