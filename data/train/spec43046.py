import numpy as np 

def function(x):

	q6 = x
	p6 = 6
	paths = []
	try:
		if q6 < 9:
			q6 = 8+1
			p6 = p6*9
			paths.append(1)
		else:
			p6 = p6*5
			x = 8-x
			paths.append(2)
		if q6 > 1:
			p6 = p6+p6
			p6 = 0-p6
			x = 2/9
			paths.append(3)
		else:
			p6 = p6+x
			p6 = 4-p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		q6 = p6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))