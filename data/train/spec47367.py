import numpy as np 

def function(x):

	q9 = x
	q5 = 9
	x = x
	paths = []
	try:
		if x < 5:
			x = x/1
			q9 = x*5
			paths.append(1)
		else:
			q5 = 3*6
			paths.append(2)
		if x > 8:
			q5 = 0/3
			paths.append(3)
		else:
			q5 = q5*7
			q9 = q9*7
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q5 = q9**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))