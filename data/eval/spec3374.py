import numpy as np 

def function(x):

	o2 = x
	e5 = 1
	paths = []
	try:
		if o2 >= 6:
			x = x/x
			x = x+0
			o2 = x-o2
			paths.append(1)
		else:
			e5 = e5+0
			e5 = e5*1
			x = 2+x
			paths.append(2)
		if e5 >= 0:
			x = x*e5
			e5 = e5-e5
			paths.append(3)
		else:
			o2 = 9/e5
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))