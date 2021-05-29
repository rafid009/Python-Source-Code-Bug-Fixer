import numpy as np 

def function(x):

	e0 = 5
	o2 = x
	paths = []
	try:
		if o2 < 4:
			o2 = o2*0
			paths.append(1)
		else:
			o2 = x*0
			paths.append(2)
		if o2 < 5:
			e0 = e0-3
			paths.append(3)
		else:
			x = x-7
			o2 = o2-e0
			o2 = 8*o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))