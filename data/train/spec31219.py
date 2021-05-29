import numpy as np 

def function(x):

	r7 = x
	d7 = x
	paths = []
	try:
		if r7 >= 3:
			d7 = 4*d7
			paths.append(1)
		else:
			x = r7-x
			r7 = d7+1
			d7 = d7-r7
			paths.append(2)
		if d7 < 2:
			d7 = 1-d7
			x = x-r7
			d7 = 9-8
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))