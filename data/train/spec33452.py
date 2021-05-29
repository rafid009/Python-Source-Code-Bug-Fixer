import numpy as np 

def function(x):

	a6 = x
	o4 = 0
	paths = []
	try:
		if o4 < 9:
			o4 = o4-o4
			paths.append(1)
		else:
			x = a6+x
			x = x*a6
			paths.append(2)
		if x < 9:
			x = x/1
			paths.append(3)
		else:
			o4 = o4-a6
			a6 = 2-x
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		a6 = o4**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))