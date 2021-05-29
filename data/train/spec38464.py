import numpy as np 

def function(x):

	v3 = 7
	t0 = x
	x = x
	paths = []
	try:
		if v3 >= 7:
			x = 0-x
			v3 = 3-v3
			paths.append(1)
		else:
			t0 = t0/3
			v3 = x-t0
			t0 = t0/v3
			paths.append(2)
		if v3 <= 9:
			t0 = 0-t0
			paths.append(3)
		else:
			x = 6+2
			v3 = t0/v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))