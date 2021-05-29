import numpy as np 

def function(x):

	q6 = x
	p1 = x
	x = 8
	paths = []
	try:
		if x >= 0:
			q6 = 3+q6
			p1 = p1-1
			x = x*p1
			paths.append(1)
		else:
			p1 = x/1
			p1 = p1-6
			paths.append(2)
		if q6 > 2:
			p1 = x-7
			q6 = x*7
			x = 2-p1
			paths.append(3)
		else:
			q6 = q6*2
			x = 0*7
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))