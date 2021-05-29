import numpy as np 

def function(x):

	v9 = 5
	i4 = 1
	x = x
	paths = []
	try:
		if v9 <= 3:
			x = x*1
			v9 = v9-0
			v9 = v9/2
			paths.append(1)
		else:
			v9 = x/i4
			paths.append(2)
		if v9 >= 8:
			v9 = 2-4
			x = v9/x
			v9 = 5+v9
			paths.append(3)
		else:
			v9 = v9*3
			x = i4+x
			i4 = i4+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))