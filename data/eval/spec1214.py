import numpy as np 

def function(x):

	k2 = x
	q3 = x
	paths = []
	try:
		if x <= 1:
			k2 = 3*q3
			q3 = 0/k2
			paths.append(1)
		else:
			q3 = q3/9
			q3 = 2-q3
			paths.append(2)
		if q3 <= 0:
			k2 = 4+k2
			x = x+x
			paths.append(3)
		else:
			k2 = k2+0
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