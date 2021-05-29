import numpy as np 

def function(x):

	j9 = x
	l6 = 3
	x = 9
	paths = []
	try:
		if j9 <= 0:
			j9 = 4-j9
			paths.append(1)
		else:
			x = x-7
			j9 = j9-j9
			paths.append(2)
		if j9 > 7:
			j9 = 2*j9
			j9 = l6/5
			l6 = 1/l6
			paths.append(3)
		else:
			j9 = j9-6
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))