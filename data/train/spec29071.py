import numpy as np 

def function(x):

	t0 = 7
	f3 = 6
	paths = []
	try:
		if t0 < 2:
			t0 = t0-x
			t0 = t0*8
			paths.append(1)
		else:
			f3 = x/3
			x = 1-x
			x = 0/4
			paths.append(2)
		if t0 > 1:
			f3 = 5+f3
			x = 8-t0
			paths.append(3)
		else:
			x = x-t0
			f3 = x-f3
			f3 = f3+8
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))