import numpy as np 

def function(x):

	q5 = x
	l6 = 2
	x = x
	paths = []
	try:
		if l6 > 9:
			x = 8+x
			q5 = 6-0
			q5 = 0+q5
			paths.append(1)
		else:
			x = q5-x
			q5 = q5/2
			paths.append(2)
		if x < 1:
			x = 5+x
			paths.append(3)
		else:
			x = l6*5
			q5 = q5-2
			q5 = q5-9
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