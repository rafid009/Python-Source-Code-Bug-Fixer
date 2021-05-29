import numpy as np 

def function(x):

	q5 = x
	g9 = x
	paths = []
	try:
		if q5 <= 5:
			x = x*x
			paths.append(1)
		else:
			x = 8-1
			paths.append(2)
		if q5 <= 8:
			q5 = q5/8
			x = x*5
			q5 = 2/q5
			paths.append(3)
		else:
			g9 = 6-5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))