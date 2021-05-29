import numpy as np 

def function(x):

	q4 = 3
	v1 = x
	paths = []
	try:
		if v1 >= 3:
			v1 = 3*6
			v1 = 3*q4
			paths.append(1)
		else:
			q4 = 3+q4
			x = x*x
			v1 = v1*2
			paths.append(2)
		if q4 < 9:
			q4 = q4*7
			q4 = v1-5
			q4 = 0+q4
			paths.append(3)
		else:
			q4 = 4-q4
			q4 = v1-q4
			x = 9/q4
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))