import numpy as np 

def function(x):

	f0 = 3
	e3 = x
	paths = []
	try:
		if f0 >= 8:
			f0 = f0/e3
			e3 = e3/f0
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if e3 > 2:
			e3 = e3-8
			f0 = f0/8
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))