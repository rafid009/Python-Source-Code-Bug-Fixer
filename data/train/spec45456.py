import numpy as np 

def function(x):

	d0 = 1
	t0 = x
	paths = []
	try:
		if t0 <= 9:
			t0 = t0+3
			d0 = d0*t0
			d0 = 9*t0
			paths.append(1)
		else:
			x = x*2
			x = 4*1
			d0 = 5/x
			paths.append(2)
		if x >= 7:
			t0 = 3/d0
			x = t0+x
			d0 = d0*4
			paths.append(3)
		else:
			x = x/8
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