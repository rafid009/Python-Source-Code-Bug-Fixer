import numpy as np 

def function(x):

	f0 = x
	paths = []
	try:
		if f0 < 5:
			f0 = x/f0
			f0 = 0*f0
			paths.append(1)
		else:
			f0 = f0*f0
			paths.append(2)
		if f0 <= 5:
			f0 = x+2
			paths.append(3)
		else:
			f0 = f0+7
			f0 = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))