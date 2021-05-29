import numpy as np 

def function(x):

	r5 = 9
	q2 = x
	paths = []
	try:
		if q2 < 2:
			q2 = r5-9
			q2 = 2-7
			x = q2*9
			paths.append(1)
		else:
			q2 = q2-x
			r5 = r5-1
			paths.append(2)
		if x >= 3:
			q2 = x*5
			x = 7-q2
			r5 = r5*0
			paths.append(3)
		else:
			r5 = 1-r5
			r5 = 9+x
			r5 = r5+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))