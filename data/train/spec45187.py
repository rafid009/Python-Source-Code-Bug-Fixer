import numpy as np 

def function(x):

	q1 = x
	t0 = x
	paths = []
	try:
		if q1 < 3:
			q1 = q1-x
			paths.append(1)
		else:
			x = 5+x
			x = x/8
			paths.append(2)
		if x <= 7:
			t0 = t0+t0
			paths.append(3)
		else:
			x = 1*x
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