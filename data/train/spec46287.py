import numpy as np 

def function(x):

	p5 = 4
	q4 = 4
	paths = []
	try:
		if x >= 6:
			p5 = 3+2
			paths.append(1)
		else:
			p5 = x+x
			p5 = p5*4
			p5 = p5*q4
			paths.append(2)
		if q4 > 4:
			x = x/x
			paths.append(3)
		else:
			q4 = 4-p5
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))