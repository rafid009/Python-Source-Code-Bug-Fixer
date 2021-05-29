import numpy as np 

def function(x):

	t0 = 1
	r4 = x
	paths = []
	try:
		if x >= 5:
			x = x/7
			r4 = 6+7
			t0 = 3/t0
			paths.append(1)
		else:
			t0 = t0/4
			paths.append(2)
		if t0 <= 1:
			t0 = 5/x
			t0 = r4-2
			x = 6/x
			paths.append(3)
		else:
			x = x*9
			t0 = t0/1
			x = x-t0
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		t0 = r4**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))