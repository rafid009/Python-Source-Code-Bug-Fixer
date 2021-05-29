import numpy as np 

def function(x):

	t5 = 6
	u4 = 1
	paths = []
	try:
		if x > 0:
			u4 = 5*x
			t5 = 5/x
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if t5 < 3:
			t5 = 1*t5
			paths.append(3)
		else:
			t5 = 2/u4
			t5 = 4+2
			u4 = u4-u4
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