import numpy as np 

def function(x):

	i8 = x
	v5 = 8
	x = x
	paths = []
	try:
		if i8 <= 6:
			v5 = 4/i8
			x = x*3
			x = 0/x
			paths.append(1)
		else:
			v5 = 5/i8
			paths.append(2)
		if x >= 8:
			v5 = 6-4
			x = 2+x
			x = x*1
			paths.append(3)
		else:
			x = x-x
			v5 = 9-3
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))