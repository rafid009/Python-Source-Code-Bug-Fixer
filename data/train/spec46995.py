import numpy as np 

def function(x):

	d2 = 0
	r1 = 7
	paths = []
	try:
		if x > 9:
			r1 = r1*1
			r1 = r1*5
			paths.append(1)
		else:
			x = r1-9
			x = x*7
			paths.append(2)
		if d2 >= 3:
			r1 = 6-r1
			paths.append(3)
		else:
			r1 = r1+r1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))