import numpy as np 

def function(x):

	t0 = x
	b7 = 5
	paths = []
	try:
		if x < 7:
			x = x/7
			x = x*b7
			x = 3+x
			paths.append(1)
		else:
			t0 = 3*t0
			paths.append(2)
		if x > 7:
			x = 4*9
			paths.append(3)
		else:
			t0 = t0-5
			t0 = 4+t0
			b7 = 1-6
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		t0 = b7**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))