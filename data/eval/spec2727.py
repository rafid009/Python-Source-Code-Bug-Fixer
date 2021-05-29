import numpy as np 

def function(x):

	q4 = 4
	n3 = x
	paths = []
	try:
		if q4 >= 4:
			q4 = q4-x
			paths.append(1)
		else:
			q4 = x*3
			q4 = q4-x
			q4 = q4+0
			paths.append(2)
		if q4 <= 1:
			q4 = q4*4
			n3 = n3-8
			n3 = n3/5
			paths.append(3)
		else:
			x = x+4
			q4 = q4-n3
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))