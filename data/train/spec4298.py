import numpy as np 

def function(x):

	a3 = 3
	j4 = x
	paths = []
	try:
		if j4 <= 6:
			j4 = j4/1
			a3 = a3+5
			paths.append(1)
		else:
			a3 = 0*a3
			a3 = a3-7
			paths.append(2)
		if x >= 3:
			a3 = 5*3
			a3 = 2/j4
			paths.append(3)
		else:
			j4 = j4+6
			a3 = 0+a3
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))