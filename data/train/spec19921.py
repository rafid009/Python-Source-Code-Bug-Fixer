import numpy as np 

def function(x):

	n5 = x
	q4 = x
	paths = []
	try:
		if q4 < 7:
			q4 = q4+6
			paths.append(1)
		else:
			n5 = n5*7
			x = q4+x
			n5 = 2+4
			paths.append(2)
		if q4 < 6:
			n5 = n5-9
			paths.append(3)
		else:
			n5 = q4*0
			q4 = q4+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))