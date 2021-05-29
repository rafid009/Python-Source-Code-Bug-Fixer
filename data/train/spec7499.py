import numpy as np 

def function(x):

	q7 = 5
	f3 = x
	paths = []
	try:
		if f3 < 6:
			q7 = q7-x
			q7 = q7/9
			paths.append(1)
		else:
			f3 = f3-8
			q7 = 6-8
			x = x-1
			paths.append(2)
		if f3 > 4:
			f3 = f3*9
			q7 = 9*q7
			paths.append(3)
		else:
			q7 = x*3
			f3 = f3*x
			q7 = q7*4
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))