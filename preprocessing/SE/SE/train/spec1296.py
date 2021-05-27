import numpy as np 

def function(x):

	t0 = x
	j4 = 0
	paths = []
	try:
		if t0 < 4:
			x = 6+0
			x = x+9
			paths.append(1)
		else:
			x = x/t0
			paths.append(2)
		if x >= 1:
			t0 = t0*t0
			t0 = 9/7
			x = x-t0
			paths.append(3)
		else:
			j4 = j4-1
			t0 = j4-t0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))