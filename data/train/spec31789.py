import numpy as np 

def function(x):

	j5 = x
	x7 = x
	paths = []
	try:
		if x < 1:
			x7 = 3+x7
			paths.append(1)
		else:
			j5 = j5*x7
			x7 = j5-3
			paths.append(2)
		if x7 <= 6:
			j5 = 2*j5
			paths.append(3)
		else:
			j5 = 2*j5
			x = x*7
			x = x-5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))