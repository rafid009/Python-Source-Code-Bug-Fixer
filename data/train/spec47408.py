import numpy as np 

def function(x):

	t4 = x
	q2 = 6
	paths = []
	try:
		if q2 <= 3:
			q2 = 6*7
			t4 = t4/q2
			paths.append(1)
		else:
			t4 = q2*t4
			t4 = 7-t4
			paths.append(2)
		if q2 >= 2:
			x = x-9
			q2 = 8+q2
			q2 = 5+q2
			paths.append(3)
		else:
			x = x*4
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))