import numpy as np 

def function(x):

	p3 = 2
	q5 = x
	paths = []
	try:
		if q5 <= 8:
			x = x+0
			paths.append(1)
		else:
			x = q5/6
			x = 6/x
			paths.append(2)
		if p3 < 6:
			x = x/p3
			paths.append(3)
		else:
			x = 9+0
			p3 = q5*p3
			q5 = 6-3
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