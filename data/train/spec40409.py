import numpy as np 

def function(x):

	f6 = 9
	v4 = 8
	paths = []
	try:
		if x < 6:
			f6 = 0-f6
			v4 = v4-1
			x = x-6
			paths.append(1)
		else:
			f6 = 0+f6
			v4 = 6-f6
			f6 = f6+4
			paths.append(2)
		if x <= 7:
			v4 = 2*v4
			f6 = x-3
			paths.append(3)
		else:
			f6 = 5+x
			f6 = x/f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))