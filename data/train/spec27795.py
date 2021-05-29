import numpy as np 

def function(x):

	q0 = x
	t4 = x
	paths = []
	try:
		if x > 9:
			t4 = t4+0
			q0 = 7/2
			paths.append(1)
		else:
			x = x+3
			t4 = 2-t4
			q0 = q0+8
			paths.append(2)
		if q0 >= 5:
			q0 = 1-x
			paths.append(3)
		else:
			t4 = 9*t4
			x = x/1
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))