import numpy as np 

def function(x):

	t0 = 8
	x9 = x
	x = 0
	paths = []
	try:
		if t0 <= 1:
			t0 = x9+t0
			paths.append(1)
		else:
			t0 = 4-t0
			x9 = t0/8
			paths.append(2)
		if x > 1:
			t0 = t0*8
			t0 = t0-1
			paths.append(3)
		else:
			x = 7+x
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