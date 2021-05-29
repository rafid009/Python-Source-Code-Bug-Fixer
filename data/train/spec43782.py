import numpy as np 

def function(x):

	q1 = 3
	p9 = 5
	paths = []
	try:
		if p9 <= 0:
			p9 = x/1
			paths.append(1)
		else:
			p9 = 0-q1
			x = x/1
			paths.append(2)
		if p9 >= 4:
			q1 = 5-q1
			x = x+7
			q1 = 6-q1
			paths.append(3)
		else:
			p9 = 3/q1
			p9 = p9+5
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