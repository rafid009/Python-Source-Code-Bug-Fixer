import numpy as np 

def function(x):

	q2 = 5
	f7 = 3
	paths = []
	try:
		if q2 <= 8:
			f7 = 2/q2
			x = x+f7
			x = x+3
			paths.append(1)
		else:
			f7 = x-6
			paths.append(2)
		if x < 7:
			x = x*2
			paths.append(3)
		else:
			x = q2+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))