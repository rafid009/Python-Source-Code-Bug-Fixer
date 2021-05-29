import numpy as np 

def function(x):

	v4 = x
	b0 = 2
	paths = []
	try:
		if x < 6:
			v4 = x-v4
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if v4 >= 4:
			v4 = v4*9
			paths.append(3)
		else:
			b0 = b0+7
			b0 = x-v4
			b0 = v4+b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		v4 = b0**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))