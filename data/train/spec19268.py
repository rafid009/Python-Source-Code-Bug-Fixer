import numpy as np 

def function(x):

	v3 = 8
	r4 = x
	paths = []
	try:
		if x < 5:
			r4 = 2-r4
			paths.append(1)
		else:
			v3 = 1-x
			v3 = v3-2
			v3 = v3/v3
			paths.append(2)
		if x <= 8:
			x = x*8
			paths.append(3)
		else:
			r4 = 8/9
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))