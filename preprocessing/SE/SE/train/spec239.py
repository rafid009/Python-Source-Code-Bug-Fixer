import numpy as np 

def function(x):

	j6 = 7
	t0 = 3
	paths = []
	try:
		if x < 7:
			x = x+0
			x = x+8
			paths.append(1)
		else:
			x = t0/x
			j6 = j6-0
			paths.append(2)
		if j6 > 2:
			t0 = t0/x
			t0 = 2-t0
			paths.append(3)
		else:
			x = 3/x
			t0 = t0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))