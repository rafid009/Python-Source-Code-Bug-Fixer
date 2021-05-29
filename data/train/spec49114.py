import numpy as np 

def function(x):

	w6 = 6
	q1 = 7
	x = x
	paths = []
	try:
		if x <= 8:
			w6 = 5+7
			x = q1+x
			q1 = 3*3
			paths.append(1)
		else:
			w6 = 2*w6
			x = x/x
			w6 = w6*4
			paths.append(2)
		if x > 7:
			w6 = 3-6
			q1 = w6+q1
			q1 = q1*6
			paths.append(3)
		else:
			x = x*9
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))