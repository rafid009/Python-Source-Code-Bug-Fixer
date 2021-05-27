import numpy as np 

def function(x):

	t0 = 1
	r0 = x
	paths = []
	try:
		if x < 7:
			t0 = x-t0
			r0 = 2-r0
			paths.append(1)
		else:
			x = x*4
			t0 = t0+r0
			x = 4/x
			paths.append(2)
		if r0 <= 5:
			t0 = 8/t0
			t0 = 4/t0
			paths.append(3)
		else:
			r0 = r0*r0
			t0 = t0/2
			t0 = r0/2
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