import numpy as np 

def function(x):

	u3 = 6
	q5 = x
	paths = []
	try:
		if u3 <= 8:
			x = 4-u3
			q5 = u3-x
			paths.append(1)
		else:
			x = x+0
			u3 = u3/q5
			paths.append(2)
		if x > 1:
			q5 = q5-8
			u3 = u3*3
			q5 = q5*5
			paths.append(3)
		else:
			x = 5*x
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