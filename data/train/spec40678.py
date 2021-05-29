import numpy as np 

def function(x):

	q2 = x
	f5 = 8
	paths = []
	try:
		if q2 < 1:
			q2 = q2+q2
			x = x-f5
			f5 = x*3
			paths.append(1)
		else:
			x = x+5
			x = x/x
			paths.append(2)
		if q2 <= 4:
			f5 = f5-5
			q2 = 6*5
			x = 0-x
			paths.append(3)
		else:
			q2 = q2-q2
			x = q2/x
			q2 = q2/4
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		q2 = f5**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))