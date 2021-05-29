import numpy as np 

def function(x):

	p5 = x
	q7 = 6
	paths = []
	try:
		if q7 >= 7:
			p5 = x-9
			q7 = 6-7
			paths.append(1)
		else:
			p5 = p5-1
			paths.append(2)
		if p5 < 5:
			q7 = 2-q7
			q7 = q7+6
			paths.append(3)
		else:
			x = q7-3
			q7 = q7+p5
			x = 9/p5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))