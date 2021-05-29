import numpy as np 

def function(x):

	y7 = x
	o4 = x
	paths = []
	try:
		if y7 <= 1:
			y7 = 8/x
			o4 = o4*0
			y7 = y7-5
			paths.append(1)
		else:
			o4 = 8/2
			y7 = y7*6
			x = 7-x
			paths.append(2)
		if o4 <= 5:
			o4 = 1-o4
			paths.append(3)
		else:
			x = x/1
			y7 = y7/5
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))