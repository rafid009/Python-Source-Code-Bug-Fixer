import numpy as np 

def function(x):

	j5 = x
	x7 = 5
	paths = []
	try:
		if x < 5:
			j5 = x+9
			x7 = x7-6
			paths.append(1)
		else:
			x7 = x*x7
			x = 9*x
			j5 = x7+5
			paths.append(2)
		if x > 0:
			x = x+j5
			paths.append(3)
		else:
			x = j5*1
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