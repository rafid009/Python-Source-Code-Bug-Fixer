import numpy as np 

def function(x):

	q6 = 8
	b0 = 0
	x = 7
	paths = []
	try:
		if b0 <= 7:
			b0 = b0-5
			paths.append(1)
		else:
			q6 = q6-x
			b0 = 5*2
			paths.append(2)
		if x >= 2:
			q6 = q6*7
			q6 = q6-b0
			x = b0+b0
			paths.append(3)
		else:
			x = 6+5
			b0 = x*b0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))