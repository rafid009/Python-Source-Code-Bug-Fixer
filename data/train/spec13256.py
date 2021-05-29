import numpy as np 

def function(x):

	q4 = 4
	f6 = 9
	paths = []
	try:
		if x <= 9:
			f6 = 6+x
			paths.append(1)
		else:
			f6 = f6+x
			paths.append(2)
		if f6 > 4:
			x = 2-x
			f6 = 1*2
			paths.append(3)
		else:
			q4 = q4-q4
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