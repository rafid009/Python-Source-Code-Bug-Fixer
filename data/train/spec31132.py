import numpy as np 

def function(x):

	o8 = x
	r8 = x
	paths = []
	try:
		if x > 2:
			o8 = 8*o8
			r8 = r8-x
			x = 4*r8
			paths.append(1)
		else:
			x = 3*x
			x = 5-x
			r8 = r8*7
			paths.append(2)
		if r8 >= 4:
			x = r8/1
			x = 5+7
			r8 = 1/r8
			paths.append(3)
		else:
			o8 = 4+o8
			r8 = 1+r8
			r8 = x*r8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))