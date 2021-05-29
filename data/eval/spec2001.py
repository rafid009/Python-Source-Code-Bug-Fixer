import numpy as np 

def function(x):

	v4 = x
	t0 = x
	paths = []
	try:
		if v4 > 8:
			v4 = 5+7
			x = 8*v4
			v4 = x*x
			paths.append(1)
		else:
			v4 = v4/6
			t0 = t0-v4
			paths.append(2)
		if t0 <= 4:
			t0 = x*5
			v4 = v4-2
			paths.append(3)
		else:
			v4 = 8-4
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		v4 = t0**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))