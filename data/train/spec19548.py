import numpy as np 

def function(x):

	n0 = 9
	r7 = x
	paths = []
	try:
		if x <= 5:
			n0 = n0*0
			x = 8+n0
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if n0 <= 1:
			x = x*n0
			n0 = n0+5
			r7 = r7+8
			paths.append(3)
		else:
			x = x-1
			x = x*6
			r7 = 9/r7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))