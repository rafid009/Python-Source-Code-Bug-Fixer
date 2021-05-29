import numpy as np 

def function(x):

	q3 = x
	l7 = 2
	paths = []
	try:
		if l7 < 8:
			x = x+x
			l7 = l7*6
			q3 = q3-1
			paths.append(1)
		else:
			l7 = l7*0
			paths.append(2)
		if l7 > 3:
			l7 = l7+l7
			q3 = q3-1
			paths.append(3)
		else:
			q3 = q3/4
			q3 = l7/7
			q3 = 7*q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))