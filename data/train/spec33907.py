import numpy as np 

def function(x):

	r9 = 6
	o5 = x
	x = x
	paths = []
	try:
		if o5 > 5:
			r9 = 3/9
			paths.append(1)
		else:
			x = 4+6
			r9 = r9/7
			x = x/9
			paths.append(2)
		if r9 < 3:
			r9 = x*r9
			x = x-7
			paths.append(3)
		else:
			r9 = 6/r9
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))