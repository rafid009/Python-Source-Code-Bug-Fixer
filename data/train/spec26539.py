import numpy as np 

def function(x):

	y4 = 0
	o5 = 9
	paths = []
	try:
		if x <= 9:
			y4 = 8-4
			y4 = y4-x
			paths.append(1)
		else:
			o5 = y4*x
			x = x*8
			o5 = 0-7
			paths.append(2)
		if x < 5:
			x = x-8
			y4 = 5*y4
			y4 = y4*0
			paths.append(3)
		else:
			y4 = y4-8
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))