import numpy as np 

def function(x):

	f6 = x
	v6 = 1
	x = x
	paths = []
	try:
		if v6 < 1:
			v6 = 5-8
			f6 = 4/v6
			f6 = f6+v6
			paths.append(1)
		else:
			v6 = v6+3
			x = 0+x
			f6 = 9/x
			paths.append(2)
		if x >= 3:
			v6 = 2/v6
			paths.append(3)
		else:
			v6 = v6-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))