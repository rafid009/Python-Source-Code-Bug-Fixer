import numpy as np 

def function(x):

	q5 = 7
	o5 = x
	paths = []
	try:
		if x > 9:
			o5 = 0/o5
			o5 = x-3
			x = x-1
			paths.append(1)
		else:
			q5 = q5-o5
			x = 1*x
			q5 = 6*q5
			paths.append(2)
		if x > 5:
			o5 = 3+8
			q5 = q5*5
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		q5 = o5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))