import numpy as np 

def function(x):

	t6 = x
	t3 = x
	x = 6
	paths = []
	try:
		if t6 <= 8:
			x = x/2
			x = t3+t3
			t6 = 0-t6
			paths.append(1)
		else:
			t6 = t6-9
			paths.append(2)
		if x < 2:
			t3 = t3/t6
			t6 = 2*t3
			t3 = t3/x
			paths.append(3)
		else:
			t3 = t3+t3
			t3 = t3/x
			x = 1-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))