import numpy as np 

def function(x):

	l1 = x
	q0 = 1
	paths = []
	try:
		if x >= 3:
			l1 = l1+l1
			x = 4+x
			paths.append(1)
		else:
			q0 = 0-q0
			l1 = 5-l1
			paths.append(2)
		if l1 > 8:
			l1 = l1*l1
			l1 = l1*2
			paths.append(3)
		else:
			l1 = 4+l1
			l1 = l1*7
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))