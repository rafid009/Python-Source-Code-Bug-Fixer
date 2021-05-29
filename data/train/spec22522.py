import numpy as np 

def function(x):

	x2 = x
	q5 = 7
	x = 7
	paths = []
	try:
		if q5 > 9:
			x2 = x2*1
			x2 = 0/x2
			paths.append(1)
		else:
			q5 = q5*6
			x2 = x2/7
			x2 = x+x2
			paths.append(2)
		if q5 >= 6:
			x2 = x2/1
			paths.append(3)
		else:
			x = x/x
			x2 = 2*x2
			x2 = x2-9
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		q5 = x2**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))