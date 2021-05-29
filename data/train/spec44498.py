import numpy as np 

def function(x):

	o1 = x
	y4 = x
	paths = []
	try:
		if x <= 4:
			y4 = 8+o1
			x = x*4
			paths.append(1)
		else:
			y4 = 0*6
			paths.append(2)
		if y4 > 0:
			y4 = y4+y4
			y4 = y4+0
			x = 3+1
			paths.append(3)
		else:
			x = x-5
			x = 1-x
			y4 = y4*y4
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))