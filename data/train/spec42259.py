import numpy as np 

def function(x):

	q5 = 2
	q0 = 0
	paths = []
	try:
		if x >= 9:
			q0 = q0*9
			x = q0*x
			paths.append(1)
		else:
			q0 = q5+q5
			q5 = q5/9
			paths.append(2)
		if x <= 8:
			q5 = q5+3
			q5 = q5+x
			q5 = 4/q5
			paths.append(3)
		else:
			q0 = q0+9
			q0 = q0+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))