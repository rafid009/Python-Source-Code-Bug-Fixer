import numpy as np 

def function(x):

	f0 = 5
	e4 = 0
	paths = []
	try:
		if e4 > 3:
			e4 = x/9
			f0 = f0-9
			paths.append(1)
		else:
			f0 = f0-1
			paths.append(2)
		if f0 <= 0:
			e4 = 8/e4
			e4 = e4-8
			e4 = e4/e4
			paths.append(3)
		else:
			e4 = e4-7
			e4 = e4/e4
			f0 = 2-0
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