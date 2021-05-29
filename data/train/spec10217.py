import numpy as np 

def function(x):

	f2 = x
	q8 = x
	paths = []
	try:
		if x <= 2:
			f2 = f2*8
			f2 = f2-6
			paths.append(1)
		else:
			x = q8-8
			f2 = q8*9
			paths.append(2)
		if x > 1:
			x = 7-0
			f2 = f2+9
			x = q8+5
			paths.append(3)
		else:
			f2 = q8*f2
			f2 = f2/1
			q8 = x*q8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))