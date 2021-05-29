import numpy as np 

def function(x):

	r5 = x
	y8 = x
	paths = []
	try:
		if r5 <= 6:
			y8 = y8*3
			x = x*3
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if r5 < 0:
			r5 = r5-0
			y8 = y8-y8
			paths.append(3)
		else:
			r5 = r5-r5
			y8 = x+y8
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		y8 = r5**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))