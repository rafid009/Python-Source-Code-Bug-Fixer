import numpy as np 

def function(x):

	x7 = x
	t0 = x
	paths = []
	try:
		if t0 > 9:
			t0 = 6/t0
			x7 = t0/x7
			t0 = t0*1
			paths.append(1)
		else:
			x7 = 6/x7
			t0 = x*1
			paths.append(2)
		if x >= 4:
			x = x+5
			x7 = 6*x7
			paths.append(3)
		else:
			x = x+8
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