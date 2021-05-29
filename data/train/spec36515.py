import numpy as np 

def function(x):

	s5 = x
	t0 = x
	paths = []
	try:
		if t0 < 7:
			x = 0*s5
			x = 7+t0
			t0 = x-1
			paths.append(1)
		else:
			t0 = t0*1
			t0 = t0-2
			x = 3/s5
			paths.append(2)
		if t0 <= 2:
			t0 = t0/1
			paths.append(3)
		else:
			x = x+4
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