import numpy as np 

def function(x):

	j7 = x
	r2 = 3
	x = x
	paths = []
	try:
		if r2 >= 3:
			j7 = j7/x
			r2 = j7*9
			paths.append(1)
		else:
			r2 = r2+1
			paths.append(2)
		if r2 <= 6:
			j7 = r2-j7
			r2 = r2/j7
			paths.append(3)
		else:
			j7 = 2-5
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