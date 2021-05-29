import numpy as np 

def function(x):

	f0 = x
	b4 = 6
	paths = []
	try:
		if f0 > 0:
			x = x+x
			f0 = 3*5
			x = 9+x
			paths.append(1)
		else:
			b4 = f0-1
			paths.append(2)
		if f0 < 9:
			x = 5/7
			paths.append(3)
		else:
			b4 = b4+8
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