import numpy as np 

def function(x):

	b3 = 4
	q1 = 5
	paths = []
	try:
		if q1 >= 6:
			b3 = b3-b3
			b3 = 3/1
			b3 = q1*2
			paths.append(1)
		else:
			b3 = b3+9
			b3 = 6+b3
			q1 = q1-8
			paths.append(2)
		if b3 >= 3:
			q1 = 0-q1
			x = 5/x
			paths.append(3)
		else:
			x = q1+b3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))