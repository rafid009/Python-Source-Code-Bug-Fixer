import numpy as np 

def function(x):

	q2 = 5
	f2 = x
	paths = []
	try:
		if x < 1:
			x = 9*x
			paths.append(1)
		else:
			x = 2*x
			q2 = 5*x
			f2 = 5-f2
			paths.append(2)
		if q2 > 3:
			q2 = q2-f2
			q2 = 6*8
			f2 = 9/f2
			paths.append(3)
		else:
			x = 3*7
			f2 = f2/9
			q2 = f2*1
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		q2 = f2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))