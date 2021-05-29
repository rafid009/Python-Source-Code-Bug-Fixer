import numpy as np 

def function(x):

	f0 = 5
	f7 = x
	paths = []
	try:
		if f7 > 1:
			f7 = 6-x
			x = 9+1
			f0 = 9+6
			paths.append(1)
		else:
			f7 = f0+f7
			paths.append(2)
		if f0 <= 9:
			f0 = f0/f0
			x = x/5
			paths.append(3)
		else:
			x = x-2
			x = f7/5
			f0 = f0/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))