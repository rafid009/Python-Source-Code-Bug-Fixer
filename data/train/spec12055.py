import numpy as np 

def function(x):

	b6 = 9
	q3 = x
	paths = []
	try:
		if q3 > 5:
			x = 9+7
			paths.append(1)
		else:
			x = b6-4
			paths.append(2)
		if q3 >= 1:
			x = q3-x
			x = x*8
			paths.append(3)
		else:
			b6 = 6*b6
			x = x+x
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))