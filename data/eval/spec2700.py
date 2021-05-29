import numpy as np 

def function(x):

	r4 = x
	n7 = x
	paths = []
	try:
		if x <= 6:
			n7 = 8*n7
			r4 = r4*1
			n7 = n7*1
			paths.append(1)
		else:
			n7 = 4+n7
			n7 = x*9
			x = n7-5
			paths.append(2)
		if n7 < 4:
			x = n7*x
			paths.append(3)
		else:
			x = 1/x
			x = 8-0
			x = 9-r4
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