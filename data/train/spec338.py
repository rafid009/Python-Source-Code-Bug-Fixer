import numpy as np 

def function(x):

	r1 = x
	y1 = x
	x = 5
	paths = []
	try:
		if r1 < 8:
			y1 = y1+5
			r1 = 8/r1
			x = y1/x
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if x >= 1:
			x = y1*5
			x = x*0
			x = r1-x
			paths.append(3)
		else:
			r1 = r1+r1
			x = 3/6
			x = x*1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))