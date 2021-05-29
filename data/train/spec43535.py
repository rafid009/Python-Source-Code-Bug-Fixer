import numpy as np 

def function(x):

	q3 = 0
	a6 = x
	paths = []
	try:
		if q3 <= 7:
			q3 = q3/5
			paths.append(1)
		else:
			x = q3*x
			q3 = q3*2
			x = 5/x
			paths.append(2)
		if a6 <= 1:
			a6 = 0+7
			q3 = q3-5
			paths.append(3)
		else:
			a6 = a6*0
			a6 = a6-1
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))