import numpy as np 

def function(x):

	v1 = 5
	f3 = x
	x = 1
	paths = []
	try:
		if x >= 7:
			v1 = v1/f3
			paths.append(1)
		else:
			x = f3*7
			paths.append(2)
		if v1 > 8:
			f3 = v1/1
			f3 = 6*f3
			v1 = f3-2
			paths.append(3)
		else:
			f3 = f3*1
			v1 = 1+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))