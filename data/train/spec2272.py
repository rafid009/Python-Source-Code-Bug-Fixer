import numpy as np 

def function(x):

	p5 = 4
	u7 = x
	paths = []
	try:
		if p5 <= 2:
			p5 = x+u7
			x = x+3
			paths.append(1)
		else:
			u7 = 9*u7
			u7 = 2*u7
			p5 = p5*u7
			paths.append(2)
		if p5 < 3:
			u7 = 4+u7
			u7 = 7+x
			p5 = 4+3
			paths.append(3)
		else:
			p5 = 3-p5
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		p5 = u7**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))