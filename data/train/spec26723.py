import numpy as np 

def function(x):

	p6 = x
	q4 = 6
	paths = []
	try:
		if p6 >= 0:
			x = 9/p6
			paths.append(1)
		else:
			p6 = p6*0
			q4 = 0+q4
			paths.append(2)
		if q4 <= 7:
			x = x+p6
			p6 = q4*x
			p6 = p6/p6
			paths.append(3)
		else:
			q4 = 5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))