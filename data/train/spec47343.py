import numpy as np 

def function(x):

	b9 = 0
	f0 = x
	paths = []
	try:
		if x > 7:
			x = x*4
			paths.append(1)
		else:
			x = x-2
			x = 3*x
			b9 = b9-0
			paths.append(2)
		if x < 9:
			x = x-f0
			x = b9-7
			f0 = x+f0
			paths.append(3)
		else:
			f0 = f0*7
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