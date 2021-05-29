import numpy as np 

def function(x):

	t1 = 1
	q6 = 1
	paths = []
	try:
		if x > 4:
			x = x/3
			x = x+t1
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if q6 >= 1:
			t1 = t1-4
			q6 = q6*6
			x = x+8
			paths.append(3)
		else:
			q6 = x/5
			q6 = 1-q6
			q6 = q6/t1
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