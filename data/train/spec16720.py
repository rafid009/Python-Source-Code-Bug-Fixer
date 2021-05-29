import numpy as np 

def function(x):

	a2 = x
	q5 = 6
	paths = []
	try:
		if a2 >= 7:
			q5 = q5-3
			q5 = q5+0
			paths.append(1)
		else:
			x = x-1
			a2 = 1-a2
			q5 = 5+q5
			paths.append(2)
		if a2 < 2:
			a2 = a2-q5
			paths.append(3)
		else:
			x = 7*x
			q5 = x+6
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		a2 = q5**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))