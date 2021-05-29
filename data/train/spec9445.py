import numpy as np 

def function(x):

	q4 = x
	j9 = 8
	paths = []
	try:
		if j9 <= 8:
			x = 8*x
			j9 = q4*j9
			q4 = j9/j9
			paths.append(1)
		else:
			j9 = 8+3
			j9 = j9*j9
			x = x+0
			paths.append(2)
		if j9 < 8:
			x = x+5
			paths.append(3)
		else:
			q4 = q4*q4
			x = 5/x
			q4 = x*x
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