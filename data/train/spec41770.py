import numpy as np 

def function(x):

	t0 = 7
	r7 = 2
	paths = []
	try:
		if r7 <= 3:
			r7 = x-t0
			r7 = 0+x
			paths.append(1)
		else:
			t0 = 7/x
			x = 7*x
			paths.append(2)
		if x <= 6:
			t0 = t0-t0
			r7 = 0-r7
			r7 = r7*7
			paths.append(3)
		else:
			x = 9+7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		t0 = r7**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))