import numpy as np 

def function(x):

	q4 = x
	e6 = 1
	paths = []
	try:
		if x <= 8:
			q4 = 0+1
			paths.append(1)
		else:
			q4 = q4/1
			q4 = 3-q4
			paths.append(2)
		if e6 > 7:
			e6 = 7-7
			q4 = 5+q4
			paths.append(3)
		else:
			e6 = e6-8
			x = x/2
			e6 = e6+5
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))