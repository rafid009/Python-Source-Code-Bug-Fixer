import numpy as np 

def function(x):

	t0 = x
	u7 = x
	x = x
	paths = []
	try:
		if u7 <= 3:
			u7 = 0/x
			x = 2/x
			x = x-x
			paths.append(1)
		else:
			t0 = t0+x
			t0 = t0+8
			paths.append(2)
		if t0 > 6:
			u7 = t0+1
			paths.append(3)
		else:
			x = x-7
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