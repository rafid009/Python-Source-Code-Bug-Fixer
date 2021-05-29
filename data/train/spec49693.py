import numpy as np 

def function(x):

	q7 = x
	l3 = x
	paths = []
	try:
		if x <= 5:
			q7 = q7/2
			paths.append(1)
		else:
			q7 = l3/1
			l3 = l3+2
			l3 = l3-q7
			paths.append(2)
		if x <= 1:
			l3 = 2/l3
			l3 = 7*0
			x = q7-x
			paths.append(3)
		else:
			l3 = l3/q7
			l3 = l3/8
			x = x-0
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