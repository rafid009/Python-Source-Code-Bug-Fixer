import numpy as np 

def function(x):

	t0 = x
	i6 = 3
	paths = []
	try:
		if i6 > 3:
			t0 = 6+t0
			paths.append(1)
		else:
			t0 = 6-9
			x = 3+x
			paths.append(2)
		if t0 <= 8:
			i6 = 5/i6
			t0 = 9/t0
			paths.append(3)
		else:
			t0 = i6/t0
			i6 = i6+x
			t0 = 9*2
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