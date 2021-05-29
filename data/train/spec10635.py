import numpy as np 

def function(x):

	p5 = 0
	q3 = 2
	paths = []
	try:
		if p5 < 4:
			p5 = 3/x
			q3 = 8/x
			q3 = 8/q3
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if x <= 1:
			p5 = 1*p5
			p5 = p5/9
			paths.append(3)
		else:
			p5 = 1*p5
			q3 = 3-p5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))