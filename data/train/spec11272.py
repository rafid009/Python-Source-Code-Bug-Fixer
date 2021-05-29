import numpy as np 

def function(x):

	w7 = 3
	t1 = 3
	paths = []
	try:
		if x <= 5:
			t1 = 7-x
			paths.append(1)
		else:
			t1 = t1*t1
			paths.append(2)
		if w7 < 8:
			t1 = 6*t1
			paths.append(3)
		else:
			x = w7+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))