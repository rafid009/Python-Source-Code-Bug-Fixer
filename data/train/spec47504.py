import numpy as np 

def function(x):

	j8 = 3
	f0 = x
	paths = []
	try:
		if f0 >= 6:
			f0 = f0/7
			j8 = j8-6
			paths.append(1)
		else:
			j8 = j8*x
			f0 = j8+j8
			x = x-8
			paths.append(2)
		if x >= 0:
			x = x-8
			x = 8+9
			x = x*2
			paths.append(3)
		else:
			x = 3-x
			x = 6/x
			f0 = f0-4
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