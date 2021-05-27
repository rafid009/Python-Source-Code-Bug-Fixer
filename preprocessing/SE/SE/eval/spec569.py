import numpy as np 

def function(x):

	j7 = 5
	l0 = 8
	paths = []
	try:
		if x <= 8:
			j7 = 6+j7
			j7 = l0/j7
			paths.append(1)
		else:
			x = 9-5
			j7 = j7*7
			x = 4/9
			paths.append(2)
		if l0 > 2:
			x = j7-x
			l0 = l0+9
			j7 = 7*j7
			paths.append(3)
		else:
			l0 = 5+0
			l0 = 3*l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))