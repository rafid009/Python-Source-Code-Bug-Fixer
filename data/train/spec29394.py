import numpy as np 

def function(x):

	t0 = x
	j5 = 7
	x = 6
	paths = []
	try:
		if x > 3:
			x = x+t0
			paths.append(1)
		else:
			t0 = t0*6
			x = 4+6
			paths.append(2)
		if j5 > 9:
			j5 = j5-2
			paths.append(3)
		else:
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))