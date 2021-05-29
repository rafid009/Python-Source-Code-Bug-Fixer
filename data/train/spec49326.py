import numpy as np 

def function(x):

	r0 = 3
	t0 = x
	paths = []
	try:
		if x > 1:
			x = x-x
			t0 = t0/t0
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if t0 < 4:
			r0 = x+r0
			paths.append(3)
		else:
			t0 = t0+0
			r0 = r0-0
			t0 = t0+2
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		r0 = t0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))