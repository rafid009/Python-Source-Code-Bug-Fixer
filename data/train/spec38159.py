import numpy as np 

def function(x):

	a7 = 1
	j9 = 0
	paths = []
	try:
		if j9 > 5:
			j9 = 9-j9
			x = 0/9
			paths.append(1)
		else:
			a7 = a7/x
			x = x*7
			j9 = 7/8
			paths.append(2)
		if j9 <= 5:
			j9 = j9/6
			a7 = a7/x
			a7 = j9/a7
			paths.append(3)
		else:
			a7 = 8+a7
			a7 = a7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))