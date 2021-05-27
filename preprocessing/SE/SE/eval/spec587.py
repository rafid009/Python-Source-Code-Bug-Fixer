import numpy as np 

def function(x):

	t4 = x
	q0 = 7
	paths = []
	try:
		if t4 < 0:
			t4 = t4/4
			q0 = q0+q0
			paths.append(1)
		else:
			q0 = q0+4
			paths.append(2)
		if t4 < 9:
			q0 = t4+6
			t4 = t4+t4
			paths.append(3)
		else:
			q0 = t4-q0
			x = x/9
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