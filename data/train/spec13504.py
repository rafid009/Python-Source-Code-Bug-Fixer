import numpy as np 

def function(x):

	b5 = 9
	q5 = x
	paths = []
	try:
		if q5 <= 1:
			b5 = 9+x
			paths.append(1)
		else:
			b5 = b5-1
			x = 7-x
			paths.append(2)
		if q5 <= 8:
			x = q5/7
			paths.append(3)
		else:
			b5 = x-x
			b5 = 0*b5
			q5 = 1+q5
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