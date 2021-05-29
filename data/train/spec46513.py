import numpy as np 

def function(x):

	j4 = x
	a7 = x
	x = 2
	paths = []
	try:
		if x < 5:
			x = j4+x
			paths.append(1)
		else:
			a7 = a7/x
			a7 = a7/a7
			j4 = a7-0
			paths.append(2)
		if a7 > 9:
			a7 = a7/a7
			j4 = 4-j4
			a7 = a7-1
			paths.append(3)
		else:
			x = x/6
			j4 = 1+j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		a7 = j4**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))