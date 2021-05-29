import numpy as np 

def function(x):

	n5 = x
	q2 = 9
	paths = []
	try:
		if x > 5:
			q2 = q2/1
			q2 = q2/q2
			x = x+3
			paths.append(1)
		else:
			q2 = 6-q2
			n5 = 4-n5
			q2 = x/q2
			paths.append(2)
		if x > 1:
			n5 = n5/4
			x = 1/x
			q2 = q2-n5
			paths.append(3)
		else:
			n5 = n5*7
			x = q2+x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		q2 = n5**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))