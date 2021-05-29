import numpy as np 

def function(x):

	k6 = 9
	t9 = x
	paths = []
	try:
		if k6 <= 1:
			k6 = 4-k6
			k6 = k6*k6
			paths.append(1)
		else:
			x = x*3
			k6 = t9/7
			paths.append(2)
		if k6 < 1:
			t9 = t9+x
			k6 = x+t9
			t9 = 4*t9
			paths.append(3)
		else:
			x = k6*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))