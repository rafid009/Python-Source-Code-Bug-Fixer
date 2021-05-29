import numpy as np 

def function(x):

	q5 = 0
	n8 = x
	paths = []
	try:
		if n8 > 6:
			q5 = q5/3
			q5 = q5/4
			paths.append(1)
		else:
			x = 3+7
			paths.append(2)
		if q5 > 9:
			x = x+x
			paths.append(3)
		else:
			x = q5/3
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		q5 = n8**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))