import numpy as np 

def function(x):

	t0 = x
	u4 = x
	paths = []
	try:
		if t0 <= 4:
			x = x/2
			u4 = u4-u4
			t0 = 0+8
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if t0 > 0:
			u4 = u4*u4
			x = x+8
			paths.append(3)
		else:
			t0 = t0-2
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