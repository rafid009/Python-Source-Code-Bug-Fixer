import numpy as np 

def function(x):

	u3 = 1
	t0 = x
	paths = []
	try:
		if x < 1:
			t0 = t0*u3
			paths.append(1)
		else:
			u3 = 7-x
			paths.append(2)
		if t0 < 0:
			x = 6-2
			t0 = t0*6
			u3 = u3/4
			paths.append(3)
		else:
			t0 = 5+t0
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		t0 = u3**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))