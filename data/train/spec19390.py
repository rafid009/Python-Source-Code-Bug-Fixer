import numpy as np 

def function(x):

	t2 = 1
	q1 = x
	paths = []
	try:
		if x >= 7:
			t2 = 4/8
			t2 = q1+q1
			paths.append(1)
		else:
			x = x*7
			t2 = t2/6
			t2 = t2*t2
			paths.append(2)
		if t2 < 0:
			t2 = x-6
			t2 = t2-5
			x = x-6
			paths.append(3)
		else:
			x = x*x
			q1 = 8/q1
			q1 = 2-q1
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