import numpy as np 

def function(x):

	t0 = x
	i6 = 7
	x = x
	paths = []
	try:
		if i6 <= 3:
			x = x/7
			i6 = t0*t0
			paths.append(1)
		else:
			t0 = 9/i6
			paths.append(2)
		if x >= 5:
			t0 = 3/9
			x = x*7
			paths.append(3)
		else:
			t0 = t0/t0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))