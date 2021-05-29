import numpy as np 

def function(x):

	t4 = x
	j5 = 8
	x = 4
	paths = []
	try:
		if x > 7:
			x = x+7
			paths.append(1)
		else:
			j5 = 1+5
			paths.append(2)
		if j5 > 4:
			j5 = j5-9
			paths.append(3)
		else:
			x = 0-x
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