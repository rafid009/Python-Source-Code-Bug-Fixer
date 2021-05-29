import numpy as np 

def function(x):

	p1 = x
	q3 = 6
	paths = []
	try:
		if p1 > 0:
			x = 7*4
			paths.append(1)
		else:
			q3 = x-0
			paths.append(2)
		if x <= 5:
			x = x+0
			paths.append(3)
		else:
			q3 = q3-q3
			p1 = p1+3
			p1 = p1-p1
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))