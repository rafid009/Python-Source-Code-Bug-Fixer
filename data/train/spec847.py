import numpy as np 

def function(x):

	q5 = x
	n7 = x
	x = x
	paths = []
	try:
		if n7 >= 5:
			x = 1-n7
			q5 = 9+q5
			q5 = 2*n7
			paths.append(1)
		else:
			n7 = n7-q5
			q5 = q5/4
			n7 = x*7
			paths.append(2)
		if x > 9:
			x = x+7
			q5 = 1/x
			n7 = n7*8
			paths.append(3)
		else:
			q5 = q5*6
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))