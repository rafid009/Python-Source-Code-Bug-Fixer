import numpy as np 

def function(x):

	b2 = x
	v2 = x
	paths = []
	try:
		if x <= 9:
			x = 6/v2
			b2 = b2+7
			x = v2/9
			paths.append(1)
		else:
			v2 = 0*v2
			paths.append(2)
		if x <= 2:
			x = x-3
			v2 = 8-v2
			x = 3+x
			paths.append(3)
		else:
			b2 = v2+3
			b2 = x/b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))