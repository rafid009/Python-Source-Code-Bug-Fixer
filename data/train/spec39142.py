import numpy as np 

def function(x):

	v7 = 3
	t0 = 3
	paths = []
	try:
		if t0 <= 0:
			t0 = 6/t0
			v7 = 0-v7
			x = 6+0
			paths.append(1)
		else:
			t0 = 0+t0
			x = x/1
			paths.append(2)
		if v7 < 2:
			x = x-7
			t0 = t0/v7
			paths.append(3)
		else:
			v7 = 5-x
			t0 = 4-v7
			t0 = t0*7
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		v7 = t0**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))