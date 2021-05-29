import numpy as np 

def function(x):

	r4 = 7
	j6 = x
	paths = []
	try:
		if j6 > 8:
			j6 = j6+7
			x = 7/x
			paths.append(1)
		else:
			j6 = j6-3
			x = 7/7
			x = x*x
			paths.append(2)
		if j6 < 3:
			j6 = 8-x
			r4 = 4-9
			paths.append(3)
		else:
			r4 = r4-j6
			x = j6-r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))