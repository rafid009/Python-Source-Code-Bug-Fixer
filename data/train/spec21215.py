import numpy as np 

def function(x):

	j5 = x
	e5 = x
	paths = []
	try:
		if j5 > 4:
			j5 = 3+8
			x = x/9
			paths.append(1)
		else:
			j5 = j5*5
			e5 = e5-j5
			paths.append(2)
		if j5 > 2:
			e5 = x*e5
			paths.append(3)
		else:
			j5 = 6+j5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))