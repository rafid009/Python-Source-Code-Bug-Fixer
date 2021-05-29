import numpy as np 

def function(x):

	v6 = 1
	f9 = x
	paths = []
	try:
		if v6 <= 7:
			f9 = f9-v6
			paths.append(1)
		else:
			x = x*1
			x = 6-0
			paths.append(2)
		if v6 > 2:
			x = 8/6
			v6 = v6+5
			paths.append(3)
		else:
			v6 = v6/x
			f9 = f9-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))