import numpy as np 

def function(x):

	j9 = x
	q2 = 0
	x = 1
	paths = []
	try:
		if q2 > 1:
			j9 = q2*7
			paths.append(1)
		else:
			x = 2*x
			x = x+q2
			paths.append(2)
		if q2 > 7:
			q2 = 5+q2
			paths.append(3)
		else:
			q2 = 6/9
			j9 = 5+j9
			j9 = 4+j9
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