import numpy as np 

def function(x):

	p5 = x
	e2 = x
	paths = []
	try:
		if x >= 7:
			x = x*4
			p5 = p5-e2
			p5 = 5+p5
			paths.append(1)
		else:
			x = x+2
			p5 = p5*9
			paths.append(2)
		if x < 4:
			p5 = 5*p5
			p5 = e2-3
			x = x+1
			paths.append(3)
		else:
			e2 = e2*e2
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		p5 = p5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))