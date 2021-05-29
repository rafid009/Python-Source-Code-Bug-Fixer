import numpy as np 

def function(x):

	q5 = x
	t8 = 1
	paths = []
	try:
		if q5 > 4:
			x = q5*x
			x = 2-x
			paths.append(1)
		else:
			t8 = 0-t8
			x = 2*q5
			q5 = 5-q5
			paths.append(2)
		if x >= 2:
			t8 = t8/4
			paths.append(3)
		else:
			x = x+1
			q5 = t8-q5
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))