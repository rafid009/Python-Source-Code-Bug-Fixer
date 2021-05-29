import numpy as np 

def function(x):

	b2 = x
	q4 = 7
	paths = []
	try:
		if b2 <= 9:
			b2 = b2+1
			b2 = b2+3
			q4 = 7/9
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if b2 > 9:
			q4 = q4*7
			q4 = x/q4
			q4 = 9*q4
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))