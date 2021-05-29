import numpy as np 

def function(x):

	t1 = x
	t0 = x
	paths = []
	try:
		if t1 < 2:
			t1 = t1+0
			x = 2-6
			x = t0-x
			paths.append(1)
		else:
			t1 = 8-2
			x = 6+x
			paths.append(2)
		if t1 >= 7:
			t1 = x-t0
			x = t0*0
			t0 = 7*6
			paths.append(3)
		else:
			t0 = t0-x
			t1 = x+t0
			t1 = t1-t1
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