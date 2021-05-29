import numpy as np 

def function(x):

	t5 = x
	q0 = x
	paths = []
	try:
		if x >= 7:
			q0 = t5/q0
			x = x-x
			paths.append(1)
		else:
			x = x+6
			t5 = t5*t5
			paths.append(2)
		if x > 1:
			q0 = 8-8
			paths.append(3)
		else:
			q0 = q0/9
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))