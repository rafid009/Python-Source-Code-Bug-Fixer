import numpy as np 

def function(x):

	q5 = 9
	n3 = x
	paths = []
	try:
		if x < 5:
			x = 4*x
			n3 = 1*n3
			x = 5/3
			paths.append(1)
		else:
			n3 = q5*6
			x = x*n3
			paths.append(2)
		if n3 < 8:
			x = n3-x
			q5 = q5+2
			q5 = 0/q5
			paths.append(3)
		else:
			n3 = n3-0
			q5 = 9-n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))