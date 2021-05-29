import numpy as np 

def function(x):

	o0 = 9
	k4 = 7
	paths = []
	try:
		if k4 <= 3:
			o0 = o0+3
			k4 = 1/9
			paths.append(1)
		else:
			o0 = o0+k4
			x = x-4
			paths.append(2)
		if k4 > 4:
			k4 = k4-6
			o0 = o0/7
			o0 = k4-k4
			paths.append(3)
		else:
			o0 = o0+o0
			o0 = k4+7
			k4 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))