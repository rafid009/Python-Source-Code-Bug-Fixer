import numpy as np 

def function(x):

	e2 = 4
	j7 = 6
	paths = []
	try:
		if e2 <= 2:
			j7 = 6-e2
			paths.append(1)
		else:
			x = x*8
			j7 = 3-j7
			j7 = j7/4
			paths.append(2)
		if j7 > 5:
			j7 = 8-e2
			j7 = j7-j7
			paths.append(3)
		else:
			x = x/e2
			j7 = j7+e2
			e2 = x*e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))