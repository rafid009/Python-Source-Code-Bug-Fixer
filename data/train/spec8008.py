import numpy as np 

def function(x):

	q5 = 4
	j6 = x
	paths = []
	try:
		if j6 <= 6:
			q5 = q5+9
			x = x+x
			q5 = q5-x
			paths.append(1)
		else:
			j6 = 7*j6
			paths.append(2)
		if x < 1:
			q5 = q5+9
			paths.append(3)
		else:
			q5 = 7*x
			q5 = 0+5
			x = x+3
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