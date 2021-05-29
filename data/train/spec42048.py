import numpy as np 

def function(x):

	b5 = x
	q3 = 8
	paths = []
	try:
		if q3 >= 5:
			b5 = b5+1
			paths.append(1)
		else:
			q3 = q3*1
			q3 = 8*b5
			paths.append(2)
		if q3 >= 8:
			b5 = b5-7
			paths.append(3)
		else:
			x = 2-8
			x = x-6
			b5 = 5+b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))