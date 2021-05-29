import numpy as np 

def function(x):

	t5 = x
	t0 = x
	paths = []
	try:
		if t0 > 2:
			t5 = 5+8
			t0 = 1*7
			paths.append(1)
		else:
			t5 = 2-2
			t0 = t5*t5
			paths.append(2)
		if t5 >= 5:
			x = 2/9
			t5 = t5+7
			t5 = 1*t5
			paths.append(3)
		else:
			t0 = t0/x
			t0 = 5-t0
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))