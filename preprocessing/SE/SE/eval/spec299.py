import numpy as np 

def function(x):

	d7 = 7
	r1 = x
	x = x
	paths = []
	try:
		if r1 <= 1:
			r1 = r1/3
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x > 4:
			x = x*x
			d7 = d7/9
			paths.append(3)
		else:
			x = x-1
			r1 = r1/d7
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