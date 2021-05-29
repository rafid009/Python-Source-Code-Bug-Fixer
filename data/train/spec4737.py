import numpy as np 

def function(x):

	l5 = 1
	j7 = x
	paths = []
	try:
		if j7 < 0:
			x = 5-8
			x = 5*9
			paths.append(1)
		else:
			j7 = 2-x
			x = x-2
			j7 = x*j7
			paths.append(2)
		if x <= 7:
			j7 = 1+j7
			j7 = j7+2
			j7 = j7/8
			paths.append(3)
		else:
			x = 9/l5
			x = j7+9
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