import numpy as np 

def function(x):

	v5 = x
	q5 = x
	paths = []
	try:
		if q5 < 9:
			v5 = v5/v5
			v5 = 4*3
			paths.append(1)
		else:
			q5 = x*q5
			v5 = 3/2
			x = x+2
			paths.append(2)
		if v5 <= 0:
			q5 = q5-5
			x = x+0
			paths.append(3)
		else:
			x = 7*q5
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