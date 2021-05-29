import numpy as np 

def function(x):

	q7 = 3
	e2 = x
	paths = []
	try:
		if q7 <= 5:
			q7 = x+4
			paths.append(1)
		else:
			q7 = q7*q7
			q7 = 9*0
			x = 1/2
			paths.append(2)
		if x <= 8:
			x = 1*q7
			x = x-e2
			paths.append(3)
		else:
			e2 = e2+1
			x = x-5
			e2 = 7*e2
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))