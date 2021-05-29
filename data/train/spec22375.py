import numpy as np 

def function(x):

	a1 = 1
	o4 = x
	paths = []
	try:
		if o4 < 0:
			o4 = o4/5
			paths.append(1)
		else:
			o4 = o4*o4
			a1 = 3-5
			o4 = o4-7
			paths.append(2)
		if a1 <= 7:
			a1 = a1/3
			x = a1+0
			a1 = 3+a1
			paths.append(3)
		else:
			x = x/3
			a1 = a1/7
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))