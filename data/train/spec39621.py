import numpy as np 

def function(x):

	q4 = 6
	v5 = x
	paths = []
	try:
		if q4 >= 8:
			x = 0+x
			x = x-v5
			q4 = 4/8
			paths.append(1)
		else:
			v5 = v5+5
			paths.append(2)
		if x >= 5:
			x = x/9
			x = v5-x
			q4 = x*x
			paths.append(3)
		else:
			v5 = 1+v5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))