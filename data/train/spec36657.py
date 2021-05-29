import numpy as np 

def function(x):

	k0 = 8
	f3 = 1
	paths = []
	try:
		if x <= 6:
			x = f3-x
			paths.append(1)
		else:
			f3 = 0*8
			f3 = f3+k0
			x = x*k0
			paths.append(2)
		if k0 > 0:
			x = x/1
			paths.append(3)
		else:
			f3 = f3-9
			x = 2*x
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