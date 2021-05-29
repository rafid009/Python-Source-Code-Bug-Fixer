import numpy as np 

def function(x):

	a5 = x
	q5 = x
	x = x
	paths = []
	try:
		if a5 > 9:
			a5 = 5*8
			a5 = a5*1
			q5 = q5/8
			paths.append(1)
		else:
			a5 = 8/a5
			x = x/9
			paths.append(2)
		if q5 < 6:
			x = 5*8
			paths.append(3)
		else:
			x = 2/x
			a5 = a5+a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))