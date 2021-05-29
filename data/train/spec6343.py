import numpy as np 

def function(x):

	q4 = x
	f4 = 5
	paths = []
	try:
		if q4 < 7:
			q4 = q4+1
			paths.append(1)
		else:
			f4 = f4-0
			q4 = q4*4
			x = x*6
			paths.append(2)
		if q4 > 9:
			f4 = f4-3
			paths.append(3)
		else:
			q4 = q4-8
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