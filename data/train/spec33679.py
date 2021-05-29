import numpy as np 

def function(x):

	h5 = 4
	f6 = x
	paths = []
	try:
		if f6 > 3:
			f6 = f6+7
			x = x*5
			paths.append(1)
		else:
			h5 = h5-9
			f6 = f6/6
			f6 = h5-f6
			paths.append(2)
		if x <= 3:
			x = 1*f6
			f6 = f6*f6
			paths.append(3)
		else:
			f6 = 5*f6
			h5 = 3*1
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))