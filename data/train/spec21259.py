import numpy as np 

def function(x):

	f9 = x
	d4 = 4
	paths = []
	try:
		if d4 >= 1:
			x = 1/x
			x = x-f9
			d4 = f9+f9
			paths.append(1)
		else:
			d4 = d4+f9
			d4 = d4*d4
			paths.append(2)
		if d4 <= 7:
			f9 = x-9
			f9 = 7*d4
			x = x-9
			paths.append(3)
		else:
			f9 = 5-f9
			d4 = d4+6
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))