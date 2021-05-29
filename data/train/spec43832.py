import numpy as np 

def function(x):

	q5 = 9
	x6 = 4
	paths = []
	try:
		if q5 <= 3:
			q5 = 8/3
			x = x/2
			paths.append(1)
		else:
			q5 = 0*6
			paths.append(2)
		if x >= 4:
			x = x/9
			x = x-9
			paths.append(3)
		else:
			q5 = q5-1
			x = q5*x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x6 = q5**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))