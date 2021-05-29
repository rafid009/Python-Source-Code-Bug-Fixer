import numpy as np 

def function(x):

	f4 = 9
	q1 = x
	paths = []
	try:
		if f4 < 2:
			x = 7*x
			x = 9*x
			paths.append(1)
		else:
			q1 = q1+f4
			paths.append(2)
		if f4 >= 1:
			x = x/q1
			q1 = q1-6
			x = x/f4
			paths.append(3)
		else:
			f4 = f4-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))