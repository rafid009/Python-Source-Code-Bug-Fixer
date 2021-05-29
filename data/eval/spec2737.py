import numpy as np 

def function(x):

	t5 = 6
	q0 = x
	paths = []
	try:
		if t5 >= 6:
			q0 = x-t5
			t5 = t5-3
			q0 = q0-0
			paths.append(1)
		else:
			t5 = t5-4
			paths.append(2)
		if q0 < 7:
			q0 = t5-q0
			t5 = x-q0
			paths.append(3)
		else:
			q0 = 7/q0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))