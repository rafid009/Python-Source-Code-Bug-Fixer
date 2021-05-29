import numpy as np 

def function(x):

	a8 = x
	q5 = x
	paths = []
	try:
		if x > 3:
			q5 = x*2
			q5 = x/q5
			paths.append(1)
		else:
			x = 5+x
			x = 7*a8
			paths.append(2)
		if q5 < 9:
			x = 5/q5
			paths.append(3)
		else:
			q5 = q5-5
			q5 = 1/q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		a8 = q5**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))