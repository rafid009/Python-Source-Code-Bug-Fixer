import numpy as np 

def function(x):

	r4 = 8
	n4 = 6
	x = 2
	paths = []
	try:
		if x <= 4:
			n4 = 3-7
			r4 = 7+n4
			paths.append(1)
		else:
			n4 = 6/5
			x = r4+x
			n4 = n4/1
			paths.append(2)
		if x < 4:
			x = 5*x
			r4 = x*r4
			paths.append(3)
		else:
			n4 = r4+3
			x = r4-2
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		r4 = n4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))