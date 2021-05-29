import numpy as np 

def function(x):

	f0 = x
	y8 = x
	paths = []
	try:
		if x < 7:
			y8 = 6/x
			x = x*2
			paths.append(1)
		else:
			f0 = f0+9
			x = x-3
			paths.append(2)
		if f0 >= 7:
			f0 = f0+0
			x = 7-3
			f0 = f0-0
			paths.append(3)
		else:
			x = f0*5
			y8 = 0+y8
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