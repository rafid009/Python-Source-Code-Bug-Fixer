import numpy as np 

def function(x):

	v5 = x
	q7 = 9
	paths = []
	try:
		if v5 <= 9:
			v5 = q7+7
			paths.append(1)
		else:
			v5 = v5+7
			paths.append(2)
		if x > 9:
			v5 = q7+0
			v5 = 5+v5
			x = x+x
			paths.append(3)
		else:
			q7 = q7-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))