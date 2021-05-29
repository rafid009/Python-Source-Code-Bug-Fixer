import numpy as np 

def function(x):

	f2 = x
	x0 = x
	x = x
	paths = []
	try:
		if x >= 3:
			x = 7+x
			x = x+x
			paths.append(1)
		else:
			f2 = x0+3
			x0 = x0*3
			paths.append(2)
		if x0 >= 8:
			x = f2+x
			x0 = x/8
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		f2 = x0**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))