import numpy as np 

def function(x):

	o1 = x
	q5 = 1
	paths = []
	try:
		if o1 >= 6:
			o1 = o1/3
			x = o1-x
			paths.append(1)
		else:
			o1 = q5/4
			o1 = o1+x
			paths.append(2)
		if o1 <= 5:
			x = 2/2
			x = o1/x
			paths.append(3)
		else:
			x = 3+q5
			o1 = o1/q5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))