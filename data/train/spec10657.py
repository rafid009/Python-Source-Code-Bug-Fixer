import numpy as np 

def function(x):

	r9 = x
	t0 = x
	paths = []
	try:
		if x <= 5:
			r9 = 3/r9
			r9 = r9/r9
			paths.append(1)
		else:
			t0 = t0+9
			paths.append(2)
		if x > 8:
			r9 = r9*r9
			paths.append(3)
		else:
			r9 = x-7
			x = x*r9
			r9 = r9*5
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		t0 = r9**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))