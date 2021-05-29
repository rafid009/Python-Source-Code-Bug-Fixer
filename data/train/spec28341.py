import numpy as np 

def function(x):

	q4 = x
	x2 = 0
	paths = []
	try:
		if q4 <= 7:
			q4 = 5+1
			q4 = q4*2
			paths.append(1)
		else:
			x = q4+3
			x = 2-x
			q4 = 6-x
			paths.append(2)
		if x2 > 8:
			x = 5+q4
			q4 = q4/1
			q4 = x+9
			paths.append(3)
		else:
			q4 = 3-q4
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