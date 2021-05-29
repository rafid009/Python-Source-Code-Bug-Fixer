import numpy as np 

def function(x):

	e7 = x
	j5 = 3
	x = x
	paths = []
	try:
		if e7 < 3:
			j5 = j5*j5
			paths.append(1)
		else:
			x = 2+1
			paths.append(2)
		if j5 <= 7:
			x = e7-8
			paths.append(3)
		else:
			j5 = e7+j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		e7 = j5**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))