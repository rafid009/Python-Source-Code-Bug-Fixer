import numpy as np 

def function(x):

	o0 = 5
	f3 = 0
	paths = []
	try:
		if x >= 2:
			o0 = 2+o0
			f3 = f3-1
			paths.append(1)
		else:
			o0 = 6*x
			f3 = f3+f3
			paths.append(2)
		if x <= 6:
			f3 = f3+x
			paths.append(3)
		else:
			f3 = 4/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))