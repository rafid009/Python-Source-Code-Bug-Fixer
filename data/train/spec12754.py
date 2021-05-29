import numpy as np 

def function(x):

	p8 = x
	j5 = 1
	paths = []
	try:
		if j5 >= 7:
			j5 = p8/j5
			j5 = j5*x
			paths.append(1)
		else:
			p8 = 7*p8
			paths.append(2)
		if x <= 6:
			p8 = p8*6
			paths.append(3)
		else:
			j5 = j5-j5
			j5 = j5-3
			x = j5*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))