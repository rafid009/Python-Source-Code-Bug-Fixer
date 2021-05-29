import numpy as np 

def function(x):

	f6 = x
	x8 = x
	x = x
	paths = []
	try:
		if f6 < 2:
			x8 = 4+3
			x = x-5
			x = x/5
			paths.append(1)
		else:
			f6 = f6/x
			x = 4/x
			f6 = f6+9
			paths.append(2)
		if x8 > 9:
			f6 = 1-1
			paths.append(3)
		else:
			f6 = f6-3
			f6 = x-f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))