import numpy as np 

def function(x):

	r5 = 9
	r4 = 1
	paths = []
	try:
		if r4 >= 0:
			r5 = 2-r5
			r4 = r5-0
			x = x-2
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x > 3:
			r5 = x*x
			paths.append(3)
		else:
			x = r4-x
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))