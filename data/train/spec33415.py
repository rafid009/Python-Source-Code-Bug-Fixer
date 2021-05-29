import numpy as np 

def function(x):

	f0 = 7
	v9 = x
	paths = []
	try:
		if x < 2:
			x = 8-3
			x = 8+v9
			v9 = 8/f0
			paths.append(1)
		else:
			f0 = f0/6
			x = x/6
			paths.append(2)
		if f0 <= 0:
			x = 7*1
			x = x*7
			paths.append(3)
		else:
			v9 = 2/v9
			v9 = v9-f0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))