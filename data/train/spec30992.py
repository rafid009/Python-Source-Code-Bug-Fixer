import numpy as np 

def function(x):

	e7 = 8
	t6 = x
	paths = []
	try:
		if x <= 5:
			e7 = t6*e7
			e7 = e7+6
			t6 = 9/t6
			paths.append(1)
		else:
			t6 = 5*t6
			t6 = t6*t6
			e7 = x/4
			paths.append(2)
		if t6 < 4:
			e7 = e7/5
			x = t6/5
			paths.append(3)
		else:
			x = 3/x
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))