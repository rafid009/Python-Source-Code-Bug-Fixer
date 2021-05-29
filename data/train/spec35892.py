import numpy as np 

def function(x):

	j4 = 8
	a1 = x
	paths = []
	try:
		if j4 <= 7:
			a1 = a1/9
			a1 = a1-x
			paths.append(1)
		else:
			j4 = x/a1
			a1 = a1-8
			x = 7/x
			paths.append(2)
		if j4 >= 3:
			x = x*9
			j4 = j4+6
			paths.append(3)
		else:
			j4 = a1+2
			a1 = a1*5
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))