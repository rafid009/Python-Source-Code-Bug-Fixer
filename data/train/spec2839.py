import numpy as np 

def function(x):

	j4 = 6
	l1 = 4
	paths = []
	try:
		if x <= 0:
			j4 = 4*l1
			x = 5+2
			l1 = 1+j4
			paths.append(1)
		else:
			l1 = l1-l1
			j4 = j4-7
			paths.append(2)
		if j4 > 5:
			j4 = j4*9
			paths.append(3)
		else:
			l1 = 7/3
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