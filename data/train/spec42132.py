import numpy as np 

def function(x):

	d5 = x
	j5 = 6
	paths = []
	try:
		if d5 < 4:
			x = 7/d5
			j5 = 9-j5
			j5 = 9-j5
			paths.append(1)
		else:
			d5 = 7-j5
			x = 1*x
			j5 = 7+j5
			paths.append(2)
		if x <= 3:
			j5 = 8/d5
			j5 = 5+j5
			d5 = 7+5
			paths.append(3)
		else:
			j5 = 6+7
			j5 = j5/x
			d5 = 9*d5
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