import numpy as np 

def function(x):

	e2 = 0
	o0 = x
	paths = []
	try:
		if x >= 9:
			x = 9/x
			e2 = e2-6
			o0 = o0+1
			paths.append(1)
		else:
			e2 = o0/9
			x = x*e2
			paths.append(2)
		if x >= 1:
			o0 = o0/7
			e2 = e2/o0
			paths.append(3)
		else:
			o0 = o0+o0
			x = 5-2
			o0 = 7+o0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))