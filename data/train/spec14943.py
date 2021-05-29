import numpy as np 

def function(x):

	t7 = 0
	q5 = x
	paths = []
	try:
		if t7 < 6:
			q5 = q5*2
			q5 = 3/6
			paths.append(1)
		else:
			t7 = t7+0
			q5 = t7+q5
			paths.append(2)
		if q5 < 6:
			q5 = t7+4
			paths.append(3)
		else:
			q5 = 0-q5
			x = t7+x
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))