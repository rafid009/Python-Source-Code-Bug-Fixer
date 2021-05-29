import numpy as np 

def function(x):

	q6 = 7
	p1 = 6
	paths = []
	try:
		if q6 > 2:
			x = 3*x
			q6 = q6/4
			paths.append(1)
		else:
			q6 = x+1
			p1 = q6/p1
			paths.append(2)
		if p1 <= 1:
			q6 = 5/5
			paths.append(3)
		else:
			p1 = x+x
			x = 9*2
			q6 = 7*5
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		q6 = p1**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))