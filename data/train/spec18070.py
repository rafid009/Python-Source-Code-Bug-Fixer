import numpy as np 

def function(x):

	b3 = 3
	r4 = 2
	paths = []
	try:
		if r4 <= 3:
			r4 = 3*r4
			r4 = r4*x
			x = x+x
			paths.append(1)
		else:
			x = 4-5
			paths.append(2)
		if b3 > 2:
			r4 = r4+0
			paths.append(3)
		else:
			b3 = b3-3
			r4 = 1/8
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