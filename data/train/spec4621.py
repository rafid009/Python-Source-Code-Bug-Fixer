import numpy as np 

def function(x):

	b6 = 7
	t0 = 9
	paths = []
	try:
		if x >= 4:
			b6 = b6*b6
			t0 = 2*t0
			x = 5*2
			paths.append(1)
		else:
			b6 = b6+3
			t0 = x/t0
			paths.append(2)
		if t0 > 1:
			t0 = 8-t0
			b6 = b6*b6
			paths.append(3)
		else:
			b6 = 7/b6
			t0 = 2/t0
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