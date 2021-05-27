import numpy as np 

def function(x):

	i4 = 5
	b3 = x
	paths = []
	try:
		if x <= 4:
			b3 = 9+7
			b3 = b3*b3
			x = x+i4
			paths.append(1)
		else:
			x = x+i4
			paths.append(2)
		if i4 < 3:
			x = i4/x
			paths.append(3)
		else:
			b3 = b3*5
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))