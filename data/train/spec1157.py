import numpy as np 

def function(x):

	q2 = x
	p9 = x
	paths = []
	try:
		if x >= 9:
			x = x-1
			paths.append(1)
		else:
			x = x+x
			q2 = 2*q2
			x = x*p9
			paths.append(2)
		if q2 < 2:
			p9 = 5/p9
			paths.append(3)
		else:
			q2 = 1*3
			p9 = p9/6
			x = p9*x
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		q2 = p9**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))