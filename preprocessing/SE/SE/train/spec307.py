import numpy as np 

def function(x):

	j6 = 9
	t0 = x
	paths = []
	try:
		if j6 >= 2:
			x = 9*x
			t0 = 8/8
			paths.append(1)
		else:
			t0 = j6*t0
			x = 9+x
			t0 = t0*9
			paths.append(2)
		if x <= 5:
			j6 = 2-2
			t0 = t0/6
			paths.append(3)
		else:
			j6 = j6-7
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))