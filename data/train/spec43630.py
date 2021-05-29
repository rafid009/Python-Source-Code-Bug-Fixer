import numpy as np 

def function(x):

	r1 = x
	y3 = x
	paths = []
	try:
		if y3 < 3:
			x = y3*0
			r1 = y3/r1
			y3 = y3/3
			paths.append(1)
		else:
			y3 = 0-r1
			y3 = 8/6
			paths.append(2)
		if y3 >= 9:
			x = 0+r1
			y3 = 5+y3
			paths.append(3)
		else:
			x = x-r1
			r1 = r1/8
			r1 = 0+4
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