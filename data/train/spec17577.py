import numpy as np 

def function(x):

	g1 = 7
	q3 = 8
	paths = []
	try:
		if q3 <= 7:
			g1 = 8+g1
			paths.append(1)
		else:
			g1 = x/g1
			x = x+0
			paths.append(2)
		if q3 < 3:
			x = x+q3
			q3 = 4/q3
			x = g1/3
			paths.append(3)
		else:
			q3 = 1-x
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		q3 = g1**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))