import numpy as np 

def function(x):

	j9 = 5
	r5 = 0
	paths = []
	try:
		if j9 > 1:
			x = x-3
			paths.append(1)
		else:
			r5 = r5+1
			x = j9*x
			j9 = j9-2
			paths.append(2)
		if r5 <= 3:
			j9 = 0+2
			j9 = j9+2
			r5 = r5-4
			paths.append(3)
		else:
			x = 9/x
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))