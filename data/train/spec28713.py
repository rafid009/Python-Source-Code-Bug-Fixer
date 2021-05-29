import numpy as np 

def function(x):

	b3 = 2
	v4 = 4
	paths = []
	try:
		if x < 1:
			x = 9+x
			v4 = v4-v4
			x = 2*x
			paths.append(1)
		else:
			x = 7-x
			b3 = b3-v4
			x = 7-1
			paths.append(2)
		if x > 8:
			b3 = 0/4
			b3 = b3+7
			paths.append(3)
		else:
			x = x*4
			x = x*x
			b3 = 7-x
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		v4 = b3**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))