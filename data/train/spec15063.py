import numpy as np 

def function(x):

	q6 = 9
	f4 = x
	paths = []
	try:
		if f4 >= 0:
			f4 = 5+f4
			f4 = f4+4
			paths.append(1)
		else:
			f4 = f4-0
			paths.append(2)
		if x > 7:
			q6 = q6+8
			paths.append(3)
		else:
			q6 = 4+f4
			f4 = q6/7
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))