import numpy as np 

def function(x):

	w5 = 3
	j6 = 6
	paths = []
	try:
		if x > 1:
			x = w5*x
			j6 = x-9
			paths.append(1)
		else:
			w5 = 1+w5
			paths.append(2)
		if j6 < 5:
			x = j6/2
			paths.append(3)
		else:
			w5 = 7-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))