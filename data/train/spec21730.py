import numpy as np 

def function(x):

	i0 = x
	t5 = x
	paths = []
	try:
		if x <= 0:
			t5 = t5/3
			paths.append(1)
		else:
			t5 = 8/t5
			t5 = x*t5
			paths.append(2)
		if x > 6:
			t5 = 4*t5
			t5 = 6/t5
			paths.append(3)
		else:
			t5 = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))