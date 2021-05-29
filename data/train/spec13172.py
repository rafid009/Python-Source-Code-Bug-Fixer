import numpy as np 

def function(x):

	r4 = 1
	t0 = 7
	paths = []
	try:
		if t0 > 9:
			r4 = r4/t0
			paths.append(1)
		else:
			r4 = 9*r4
			x = x+1
			paths.append(2)
		if r4 > 8:
			r4 = r4-9
			r4 = r4*4
			t0 = t0/5
			paths.append(3)
		else:
			x = t0/4
			r4 = r4*r4
			r4 = t0+x
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