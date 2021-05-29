import numpy as np 

def function(x):

	r0 = x
	y6 = 2
	paths = []
	try:
		if x <= 9:
			y6 = 4+y6
			paths.append(1)
		else:
			y6 = r0/6
			paths.append(2)
		if y6 < 9:
			y6 = y6+8
			r0 = x+1
			paths.append(3)
		else:
			r0 = r0+6
			y6 = y6/x
			x = 5/6
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		y6 = r0**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))