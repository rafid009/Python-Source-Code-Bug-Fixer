import numpy as np 

def function(x):

	q1 = 1
	o2 = 4
	paths = []
	try:
		if q1 >= 3:
			o2 = o2*8
			paths.append(1)
		else:
			o2 = q1/9
			paths.append(2)
		if q1 < 5:
			q1 = q1*o2
			o2 = o2+3
			paths.append(3)
		else:
			x = o2+x
			q1 = x*o2
			q1 = q1*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))