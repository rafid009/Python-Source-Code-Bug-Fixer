import numpy as np 

def function(x):

	p6 = x
	q7 = 8
	paths = []
	try:
		if x > 7:
			q7 = q7-8
			p6 = 8*8
			paths.append(1)
		else:
			q7 = q7+3
			x = x-5
			p6 = 9-5
			paths.append(2)
		if q7 < 4:
			x = p6*2
			p6 = p6-p6
			paths.append(3)
		else:
			p6 = p6-q7
			p6 = 9/p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		q7 = p6**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))