import numpy as np 

def function(x):

	h9 = x
	f0 = x
	paths = []
	try:
		if x <= 1:
			h9 = 5-h9
			f0 = f0*2
			h9 = 3-7
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x > 3:
			f0 = x*f0
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))