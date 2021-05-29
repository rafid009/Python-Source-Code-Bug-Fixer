import numpy as np 

def function(x):

	g3 = x
	q1 = 4
	paths = []
	try:
		if g3 < 5:
			x = x-7
			paths.append(1)
		else:
			g3 = 2+x
			q1 = q1*0
			paths.append(2)
		if g3 < 4:
			x = 0-x
			q1 = q1/3
			x = x+g3
			paths.append(3)
		else:
			q1 = q1-4
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