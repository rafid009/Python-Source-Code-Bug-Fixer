import numpy as np 

def function(x):

	j8 = 9
	f0 = 6
	paths = []
	try:
		if f0 < 9:
			j8 = j8/x
			j8 = j8+0
			f0 = j8-f0
			paths.append(1)
		else:
			x = x*6
			f0 = f0*j8
			x = x*x
			paths.append(2)
		if f0 > 4:
			f0 = 3-f0
			f0 = f0-3
			paths.append(3)
		else:
			j8 = j8-4
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))