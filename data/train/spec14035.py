import numpy as np 

def function(x):

	i6 = 2
	t0 = x
	paths = []
	try:
		if i6 < 8:
			i6 = t0/i6
			i6 = x-x
			i6 = 7-i6
			paths.append(1)
		else:
			i6 = i6*9
			paths.append(2)
		if t0 < 4:
			x = i6+5
			i6 = t0-i6
			i6 = i6-2
			paths.append(3)
		else:
			x = x/i6
			t0 = t0-6
			x = 6-t0
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))