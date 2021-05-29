import numpy as np 

def function(x):

	q7 = 9
	u4 = x
	paths = []
	try:
		if x <= 0:
			x = x/2
			q7 = 5-9
			x = 6-q7
			paths.append(1)
		else:
			q7 = 1*0
			q7 = 3-1
			paths.append(2)
		if q7 <= 2:
			u4 = 1-u4
			x = 4+8
			u4 = u4-u4
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))