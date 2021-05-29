import numpy as np 

def function(x):

	u0 = x
	t6 = 9
	x = 7
	paths = []
	try:
		if u0 >= 1:
			t6 = 4*t6
			paths.append(1)
		else:
			t6 = t6-9
			paths.append(2)
		if u0 < 5:
			t6 = t6-x
			x = 6+x
			t6 = 9+8
			paths.append(3)
		else:
			x = 4*1
			u0 = u0-3
			x = 9+0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))