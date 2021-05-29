import numpy as np 

def function(x):

	l5 = 5
	t0 = 2
	paths = []
	try:
		if t0 < 6:
			t0 = t0/6
			x = x*l5
			t0 = t0*x
			paths.append(1)
		else:
			l5 = t0-l5
			paths.append(2)
		if x < 0:
			t0 = 3+t0
			l5 = 5-l5
			paths.append(3)
		else:
			t0 = 1/t0
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