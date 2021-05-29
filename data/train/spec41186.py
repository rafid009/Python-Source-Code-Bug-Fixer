import numpy as np 

def function(x):

	f9 = 6
	q2 = 9
	paths = []
	try:
		if f9 < 3:
			f9 = 1+f9
			paths.append(1)
		else:
			x = f9+x
			paths.append(2)
		if x < 5:
			f9 = 1+1
			f9 = q2+f9
			paths.append(3)
		else:
			x = 6-x
			x = 8-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))