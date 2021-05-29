import numpy as np 

def function(x):

	j1 = 9
	o3 = x
	paths = []
	try:
		if j1 >= 9:
			j1 = j1+8
			paths.append(1)
		else:
			x = 5-4
			j1 = j1+9
			x = o3/o3
			paths.append(2)
		if o3 <= 4:
			j1 = 1-4
			paths.append(3)
		else:
			o3 = x-o3
			x = 9*1
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