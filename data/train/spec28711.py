import numpy as np 

def function(x):

	q2 = 9
	d9 = x
	x = 9
	paths = []
	try:
		if x > 2:
			d9 = d9*7
			d9 = d9*2
			paths.append(1)
		else:
			x = d9-x
			q2 = 1+8
			q2 = q2-q2
			paths.append(2)
		if d9 > 9:
			x = x*9
			x = x*q2
			paths.append(3)
		else:
			q2 = q2*9
			q2 = q2/q2
			d9 = d9+0
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		q2 = d9**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))