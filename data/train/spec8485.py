import numpy as np 

def function(x):

	w2 = x
	r4 = 7
	paths = []
	try:
		if x > 5:
			x = x*w2
			paths.append(1)
		else:
			r4 = r4*x
			paths.append(2)
		if x < 8:
			r4 = 1*r4
			x = x-0
			x = 9/x
			paths.append(3)
		else:
			r4 = 6*7
			x = x/x
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