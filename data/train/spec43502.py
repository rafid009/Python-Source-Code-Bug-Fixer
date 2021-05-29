import numpy as np 

def function(x):

	q8 = x
	p9 = 2
	x = 7
	paths = []
	try:
		if p9 > 6:
			q8 = q8-q8
			q8 = x+q8
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if x <= 0:
			p9 = 9+2
			q8 = 7/q8
			x = q8+4
			paths.append(3)
		else:
			p9 = x+3
			p9 = 1+p9
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))