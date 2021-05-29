import numpy as np 

def function(x):

	x6 = x
	f0 = x
	paths = []
	try:
		if x6 > 2:
			f0 = 9*x6
			x6 = x6+x6
			paths.append(1)
		else:
			x = x6*x
			paths.append(2)
		if f0 <= 9:
			x6 = f0-2
			paths.append(3)
		else:
			x6 = x6/f0
			x = f0-x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		f0 = x6**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))