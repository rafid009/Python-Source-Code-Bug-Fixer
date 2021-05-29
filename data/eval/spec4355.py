import numpy as np 

def function(x):

	t0 = x
	v0 = x
	x = 0
	paths = []
	try:
		if v0 < 6:
			v0 = 7-v0
			paths.append(1)
		else:
			x = x*2
			x = t0-x
			v0 = v0/x
			paths.append(2)
		if x < 9:
			t0 = t0+x
			paths.append(3)
		else:
			v0 = 5-t0
			t0 = t0-3
			x = x-7
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