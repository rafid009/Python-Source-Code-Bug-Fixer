import numpy as np 

def function(x):

	q5 = 7
	t3 = x
	paths = []
	try:
		if x < 6:
			x = 6*9
			x = x+2
			x = 3+x
			paths.append(1)
		else:
			q5 = x-q5
			paths.append(2)
		if x >= 8:
			x = x/2
			q5 = 1/q5
			paths.append(3)
		else:
			q5 = 6-q5
			t3 = x*t3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		q5 = t3**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))