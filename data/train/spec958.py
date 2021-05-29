import numpy as np 

def function(x):

	j5 = 7
	q3 = 9
	x = 6
	paths = []
	try:
		if x >= 8:
			j5 = 4*5
			j5 = x+7
			x = x-0
			paths.append(1)
		else:
			x = 6*j5
			j5 = 0-j5
			paths.append(2)
		if j5 < 5:
			x = x-7
			q3 = q3+0
			paths.append(3)
		else:
			j5 = 5+j5
			j5 = j5*9
			q3 = 0*x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		q3 = j5**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))