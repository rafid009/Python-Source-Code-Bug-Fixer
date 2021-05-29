import numpy as np 

def function(x):

	t6 = x
	k6 = x
	paths = []
	try:
		if x <= 3:
			x = x+4
			k6 = k6+k6
			paths.append(1)
		else:
			t6 = 4*t6
			k6 = k6*6
			k6 = k6+0
			paths.append(2)
		if x > 7:
			k6 = k6+7
			k6 = 4+9
			paths.append(3)
		else:
			k6 = k6/2
			k6 = 2*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))