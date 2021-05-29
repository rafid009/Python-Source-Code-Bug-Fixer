import numpy as np 

def function(x):

	i0 = 9
	f9 = 1
	paths = []
	try:
		if f9 > 4:
			i0 = 8*i0
			i0 = 9*i0
			i0 = i0*x
			paths.append(1)
		else:
			x = x*i0
			x = 6-x
			paths.append(2)
		if i0 > 1:
			i0 = i0/f9
			paths.append(3)
		else:
			x = i0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))