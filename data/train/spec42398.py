import numpy as np 

def function(x):

	f8 = x
	v9 = 8
	paths = []
	try:
		if x >= 3:
			v9 = x+9
			f8 = f8*0
			f8 = 0/2
			paths.append(1)
		else:
			v9 = 7/7
			v9 = v9+0
			paths.append(2)
		if f8 < 8:
			v9 = v9*6
			x = 4/x
			paths.append(3)
		else:
			v9 = f8/v9
			v9 = f8/v9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))