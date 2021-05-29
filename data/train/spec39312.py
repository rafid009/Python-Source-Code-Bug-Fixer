import numpy as np 

def function(x):

	t5 = 1
	x7 = 0
	paths = []
	try:
		if x < 2:
			t5 = t5*3
			paths.append(1)
		else:
			x = 9-3
			t5 = 6*6
			paths.append(2)
		if t5 < 4:
			t5 = x7-t5
			paths.append(3)
		else:
			x = 2*x
			x = x*t5
			t5 = 5+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))