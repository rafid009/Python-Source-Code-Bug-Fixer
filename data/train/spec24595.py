import numpy as np 

def function(x):

	f3 = 8
	k2 = x
	paths = []
	try:
		if x >= 7:
			x = 5+0
			x = k2*x
			k2 = k2/k2
			paths.append(1)
		else:
			f3 = f3*f3
			paths.append(2)
		if f3 >= 8:
			f3 = k2+4
			paths.append(3)
		else:
			x = 5/x
			x = f3-5
			k2 = f3/k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))