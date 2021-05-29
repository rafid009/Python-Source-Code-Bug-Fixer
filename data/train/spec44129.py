import numpy as np 

def function(x):

	y6 = x
	r7 = x
	paths = []
	try:
		if y6 < 0:
			y6 = y6/y6
			r7 = 2/r7
			x = r7/7
			paths.append(1)
		else:
			r7 = r7+y6
			x = 9-x
			y6 = y6*1
			paths.append(2)
		if x <= 6:
			r7 = x*9
			r7 = r7-0
			paths.append(3)
		else:
			r7 = 1+1
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