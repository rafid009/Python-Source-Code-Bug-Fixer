import numpy as np 

def function(x):

	e3 = 1
	q1 = x
	paths = []
	try:
		if q1 <= 9:
			x = 6+x
			e3 = e3+x
			x = 6/7
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x < 4:
			e3 = 6+e3
			x = x/9
			q1 = 4+q1
			paths.append(3)
		else:
			e3 = 3/q1
			q1 = 8+x
			q1 = x+3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))