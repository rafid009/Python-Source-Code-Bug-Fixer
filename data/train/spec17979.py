import numpy as np 

def function(x):

	t0 = 3
	i6 = x
	paths = []
	try:
		if x >= 8:
			x = 1-2
			x = 3/t0
			paths.append(1)
		else:
			x = x/9
			i6 = i6*x
			i6 = i6+i6
			paths.append(2)
		if t0 < 7:
			t0 = 9+t0
			i6 = i6-5
			paths.append(3)
		else:
			i6 = 9-i6
			i6 = i6*t0
			t0 = 4+0
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