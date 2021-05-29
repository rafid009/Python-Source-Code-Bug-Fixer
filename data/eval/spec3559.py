import numpy as np 

def function(x):

	q9 = x
	f0 = x
	paths = []
	try:
		if q9 > 4:
			x = 1/2
			paths.append(1)
		else:
			f0 = f0+7
			paths.append(2)
		if f0 < 6:
			x = x*q9
			f0 = 7*f0
			f0 = f0*4
			paths.append(3)
		else:
			x = q9+x
			q9 = 7+2
			q9 = q9*8
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))