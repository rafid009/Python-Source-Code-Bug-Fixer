import numpy as np 

def function(x):

	f6 = 3
	i4 = x
	paths = []
	try:
		if f6 <= 7:
			i4 = i4-6
			paths.append(1)
		else:
			f6 = f6/2
			f6 = 9-f6
			x = x-7
			paths.append(2)
		if f6 < 4:
			f6 = f6/x
			x = 7+x
			x = x+4
			paths.append(3)
		else:
			f6 = 9+i4
			f6 = 5-f6
			f6 = 5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))