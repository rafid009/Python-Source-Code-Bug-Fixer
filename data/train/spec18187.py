import numpy as np 

def function(x):

	o2 = x
	e7 = 4
	paths = []
	try:
		if x > 5:
			x = 7/o2
			paths.append(1)
		else:
			e7 = 4-2
			e7 = 8+0
			paths.append(2)
		if x < 4:
			o2 = x*2
			e7 = o2*e7
			e7 = 5/2
			paths.append(3)
		else:
			x = o2-x
			o2 = o2/9
			e7 = e7/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))