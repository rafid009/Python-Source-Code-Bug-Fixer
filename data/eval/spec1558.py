import numpy as np 

def function(x):

	f6 = 8
	j2 = 7
	paths = []
	try:
		if j2 > 6:
			j2 = 0/j2
			paths.append(1)
		else:
			f6 = 3/f6
			paths.append(2)
		if j2 >= 3:
			f6 = f6/6
			j2 = 5/8
			x = x+1
			paths.append(3)
		else:
			f6 = 4*x
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