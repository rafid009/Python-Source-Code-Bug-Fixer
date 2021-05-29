import numpy as np 

def function(x):

	q7 = x
	f4 = x
	paths = []
	try:
		if q7 <= 6:
			f4 = f4-8
			f4 = f4*1
			paths.append(1)
		else:
			x = 4+7
			q7 = q7-3
			x = 5*5
			paths.append(2)
		if x >= 2:
			f4 = f4*1
			q7 = x*8
			q7 = q7-6
			paths.append(3)
		else:
			q7 = q7-0
			f4 = 5-f4
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		q7 = f4**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))