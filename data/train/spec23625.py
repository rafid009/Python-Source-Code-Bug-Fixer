import numpy as np 

def function(x):

	e2 = x
	p5 = 1
	paths = []
	try:
		if e2 > 1:
			e2 = 5/p5
			e2 = 2/p5
			paths.append(1)
		else:
			x = x+6
			p5 = p5*7
			paths.append(2)
		if x > 2:
			p5 = p5*2
			e2 = e2+x
			x = 1-0
			paths.append(3)
		else:
			e2 = 6*e2
			e2 = 0+x
			e2 = e2/p5
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))