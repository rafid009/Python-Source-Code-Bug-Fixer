import numpy as np 

def function(x):

	i0 = x
	j1 = 4
	paths = []
	try:
		if i0 >= 7:
			x = j1*9
			j1 = x*j1
			paths.append(1)
		else:
			j1 = i0/i0
			x = i0*1
			paths.append(2)
		if x >= 2:
			i0 = i0*i0
			j1 = 3*4
			paths.append(3)
		else:
			x = x-9
			i0 = 8/i0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))