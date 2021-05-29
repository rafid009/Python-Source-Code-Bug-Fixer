import numpy as np 

def function(x):

	b0 = x
	q0 = x
	paths = []
	try:
		if x < 7:
			q0 = q0*9
			paths.append(1)
		else:
			q0 = 9*3
			x = 5/2
			b0 = b0*1
			paths.append(2)
		if q0 < 0:
			x = b0+x
			b0 = b0*2
			paths.append(3)
		else:
			x = 9+x
			x = q0/x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))