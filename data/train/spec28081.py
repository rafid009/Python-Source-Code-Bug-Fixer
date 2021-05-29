import numpy as np 

def function(x):

	r5 = 4
	e7 = x
	x = x
	paths = []
	try:
		if x > 2:
			x = x-1
			r5 = r5*0
			e7 = e7*r5
			paths.append(1)
		else:
			r5 = r5+6
			r5 = r5-5
			x = 1*7
			paths.append(2)
		if x <= 4:
			x = e7-x
			r5 = 2*0
			r5 = x-x
			paths.append(3)
		else:
			r5 = 7-r5
			r5 = 6/8
			r5 = 0+r5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))