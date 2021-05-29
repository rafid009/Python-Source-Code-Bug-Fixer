import numpy as np 

def function(x):

	t0 = x
	b9 = 4
	paths = []
	try:
		if t0 <= 2:
			b9 = b9+3
			paths.append(1)
		else:
			t0 = 6-t0
			t0 = 3/1
			t0 = 7+t0
			paths.append(2)
		if b9 < 1:
			t0 = 8/9
			paths.append(3)
		else:
			b9 = b9+0
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))