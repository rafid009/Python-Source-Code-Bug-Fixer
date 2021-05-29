import numpy as np 

def function(x):

	t5 = 8
	q6 = x
	x = x
	paths = []
	try:
		if x >= 9:
			x = 0+x
			q6 = t5*x
			x = x-7
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if q6 < 7:
			x = x-t5
			paths.append(3)
		else:
			x = x*t5
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		t5 = q6**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))