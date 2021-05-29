import numpy as np 

def function(x):

	r4 = 7
	n7 = 9
	x = 5
	paths = []
	try:
		if x <= 8:
			x = 3-x
			r4 = r4+2
			x = x*5
			paths.append(1)
		else:
			r4 = r4*3
			r4 = r4*8
			n7 = n7/2
			paths.append(2)
		if x < 4:
			r4 = 8-r4
			n7 = r4+n7
			r4 = n7/r4
			paths.append(3)
		else:
			n7 = n7*6
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