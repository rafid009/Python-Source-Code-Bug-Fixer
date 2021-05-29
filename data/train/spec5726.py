import numpy as np 

def function(x):

	r5 = x
	x8 = x
	x = 9
	paths = []
	try:
		if r5 > 7:
			x8 = x8*9
			paths.append(1)
		else:
			x8 = 2+r5
			x = 4-r5
			paths.append(2)
		if x > 2:
			r5 = x/9
			r5 = 1-2
			paths.append(3)
		else:
			x8 = 7-x8
			r5 = r5*6
			x = r5/2
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))