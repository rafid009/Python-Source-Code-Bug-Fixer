import numpy as np 

def function(x):

	j9 = 0
	q5 = 8
	x = x
	paths = []
	try:
		if q5 > 1:
			j9 = j9+x
			paths.append(1)
		else:
			q5 = 9*q5
			q5 = q5/x
			q5 = 2+x
			paths.append(2)
		if j9 > 0:
			x = 3/x
			paths.append(3)
		else:
			q5 = q5+1
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