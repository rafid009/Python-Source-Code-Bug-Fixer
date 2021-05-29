import numpy as np 

def function(x):

	q6 = x
	n3 = x
	paths = []
	try:
		if q6 < 4:
			n3 = n3-8
			q6 = q6*6
			q6 = 5/7
			paths.append(1)
		else:
			x = x/x
			n3 = 1+n3
			paths.append(2)
		if x > 3:
			q6 = x+6
			n3 = 2/n3
			q6 = q6+8
			paths.append(3)
		else:
			n3 = x+9
			q6 = q6*4
			q6 = 7-q6
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