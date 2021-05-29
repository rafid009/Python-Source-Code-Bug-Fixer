import numpy as np 

def function(x):

	q3 = x
	b9 = 2
	paths = []
	try:
		if q3 <= 4:
			q3 = q3*q3
			b9 = q3-7
			paths.append(1)
		else:
			x = x+b9
			q3 = q3*b9
			x = x+x
			paths.append(2)
		if x < 0:
			b9 = b9/x
			paths.append(3)
		else:
			x = 0*x
			q3 = b9+6
			b9 = 7/4
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))