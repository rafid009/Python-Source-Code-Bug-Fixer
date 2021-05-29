import numpy as np 

def function(x):

	q9 = x
	p5 = 1
	paths = []
	try:
		if p5 > 1:
			p5 = 4-6
			q9 = 0-2
			q9 = x*q9
			paths.append(1)
		else:
			p5 = 0/5
			x = 4+x
			p5 = p5-2
			paths.append(2)
		if q9 <= 4:
			q9 = 6-p5
			paths.append(3)
		else:
			x = 5-x
			q9 = q9+5
			x = 9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p5 = x**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))