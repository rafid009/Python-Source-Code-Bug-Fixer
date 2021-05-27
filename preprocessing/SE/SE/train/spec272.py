import numpy as np 

def function(x):

	q4 = 3
	t1 = 1
	paths = []
	try:
		if x > 6:
			q4 = q4+x
			x = 1-x
			t1 = t1+5
			paths.append(1)
		else:
			t1 = q4*t1
			q4 = q4-1
			t1 = 3+q4
			paths.append(2)
		if t1 < 0:
			x = t1+5
			paths.append(3)
		else:
			x = x+0
			x = 4+x
			q4 = 5/q4
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