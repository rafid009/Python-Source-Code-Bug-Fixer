import numpy as np 

def function(x):

	z1 = x
	f6 = x
	paths = []
	try:
		if f6 > 7:
			x = x-2
			x = x*4
			f6 = 0*4
			paths.append(1)
		else:
			f6 = f6*z1
			paths.append(2)
		if x >= 1:
			x = 3-x
			x = 0*z1
			paths.append(3)
		else:
			f6 = f6/z1
			x = 2/z1
			f6 = f6+6
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		f6 = z1**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))