import numpy as np 

def function(x):

	f0 = x
	e0 = x
	paths = []
	try:
		if x <= 8:
			f0 = x/2
			paths.append(1)
		else:
			e0 = e0*e0
			f0 = 5/3
			paths.append(2)
		if x >= 3:
			e0 = 6+2
			paths.append(3)
		else:
			f0 = f0+2
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))