import numpy as np 

def function(x):

	t0 = 8
	p8 = x
	x = 8
	paths = []
	try:
		if t0 <= 0:
			x = 2/p8
			paths.append(1)
		else:
			t0 = t0+3
			paths.append(2)
		if t0 >= 1:
			p8 = 3+p8
			paths.append(3)
		else:
			x = x-2
			t0 = 3*t0
			p8 = p8-8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		t0 = p8**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))