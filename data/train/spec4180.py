import numpy as np 

def function(x):

	j3 = 7
	r4 = x
	paths = []
	try:
		if j3 > 0:
			r4 = 2/r4
			x = x+3
			paths.append(1)
		else:
			r4 = 2-r4
			r4 = 7/r4
			r4 = r4+7
			paths.append(2)
		if r4 > 2:
			x = x*8
			r4 = r4/8
			x = x+2
			paths.append(3)
		else:
			r4 = r4-4
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