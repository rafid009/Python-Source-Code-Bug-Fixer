import numpy as np 

def function(x):

	f6 = 5
	f0 = x
	paths = []
	try:
		if f0 >= 2:
			x = f6*2
			f6 = 6/f6
			paths.append(1)
		else:
			x = x-f6
			paths.append(2)
		if f6 < 5:
			f6 = 2+f6
			f0 = 8/f0
			x = 7+x
			paths.append(3)
		else:
			f6 = 8+f6
			f6 = 8/f6
			f6 = f6*f6
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))