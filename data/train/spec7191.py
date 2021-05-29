import numpy as np 

def function(x):

	r8 = x
	o8 = 8
	paths = []
	try:
		if o8 > 1:
			o8 = o8-r8
			paths.append(1)
		else:
			r8 = r8-x
			paths.append(2)
		if r8 >= 2:
			x = x-1
			o8 = 6/o8
			r8 = 5/r8
			paths.append(3)
		else:
			r8 = r8/7
			r8 = x*1
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))