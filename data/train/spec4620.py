import numpy as np 

def function(x):

	q1 = 2
	t0 = 9
	paths = []
	try:
		if t0 <= 3:
			t0 = q1*6
			t0 = t0+q1
			paths.append(1)
		else:
			t0 = t0/t0
			paths.append(2)
		if q1 < 0:
			t0 = t0+1
			paths.append(3)
		else:
			q1 = 5/x
			q1 = 5/q1
			x = 2*9
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))