import numpy as np 

def function(x):

	q6 = 1
	t1 = x
	paths = []
	try:
		if q6 < 7:
			x = t1/q6
			t1 = 6/t1
			paths.append(1)
		else:
			x = t1*t1
			q6 = 3+x
			q6 = 5*7
			paths.append(2)
		if t1 >= 2:
			q6 = 7-t1
			x = 0-x
			paths.append(3)
		else:
			q6 = t1/q6
			t1 = t1/8
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))