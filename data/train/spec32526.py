import numpy as np 

def function(x):

	q7 = x
	r5 = 4
	paths = []
	try:
		if q7 >= 7:
			x = 9/9
			r5 = r5/2
			r5 = q7+9
			paths.append(1)
		else:
			x = 3+2
			x = x+8
			paths.append(2)
		if q7 > 5:
			x = x+7
			r5 = x/r5
			paths.append(3)
		else:
			q7 = q7-0
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		r5 = q7**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))