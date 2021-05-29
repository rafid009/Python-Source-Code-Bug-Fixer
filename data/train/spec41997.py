import numpy as np 

def function(x):

	p1 = 6
	q1 = 5
	paths = []
	try:
		if x < 4:
			p1 = p1/9
			paths.append(1)
		else:
			x = 6/x
			p1 = 2-p1
			x = p1*4
			paths.append(2)
		if q1 >= 4:
			x = p1+x
			x = 8*x
			paths.append(3)
		else:
			q1 = 6+8
			x = x+q1
			x = 7*x
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