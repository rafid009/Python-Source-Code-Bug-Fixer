import numpy as np 

def function(x):

	q6 = x
	p6 = x
	paths = []
	try:
		if p6 >= 3:
			p6 = q6+x
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if q6 < 4:
			q6 = p6+5
			q6 = x-8
			paths.append(3)
		else:
			x = x-q6
			p6 = p6/2
			q6 = q6-1
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))