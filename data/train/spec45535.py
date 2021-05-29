import numpy as np 

def function(x):

	r1 = x
	d7 = 0
	paths = []
	try:
		if d7 >= 3:
			x = 8/d7
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if r1 > 2:
			d7 = 5-5
			x = 9*d7
			r1 = x*2
			paths.append(3)
		else:
			r1 = r1+3
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))