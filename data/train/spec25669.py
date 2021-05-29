import numpy as np 

def function(x):

	t0 = x
	q3 = x
	paths = []
	try:
		if q3 < 4:
			t0 = 3+8
			q3 = q3+q3
			paths.append(1)
		else:
			q3 = q3+0
			t0 = t0-6
			paths.append(2)
		if t0 <= 7:
			x = x+3
			x = 6/9
			t0 = t0-x
			paths.append(3)
		else:
			q3 = 1/q3
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))