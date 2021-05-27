import numpy as np 

def function(x):

	q1 = 0
	t6 = x
	paths = []
	try:
		if q1 >= 4:
			q1 = q1+7
			x = x+q1
			paths.append(1)
		else:
			t6 = t6*7
			paths.append(2)
		if x < 1:
			x = x+8
			x = x-0
			paths.append(3)
		else:
			t6 = 5+t6
			x = x/t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))