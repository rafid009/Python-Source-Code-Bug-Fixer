import numpy as np 

def function(x):

	f0 = x
	j7 = x
	x = 5
	paths = []
	try:
		if x <= 6:
			f0 = f0-1
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if x <= 7:
			x = x+x
			f0 = 1-9
			x = x*x
			paths.append(3)
		else:
			j7 = j7-1
			x = 8-4
			j7 = j7-f0
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))