import numpy as np 

def function(x):

	x2 = 7
	p5 = x
	paths = []
	try:
		if p5 <= 9:
			x2 = p5/6
			paths.append(1)
		else:
			x2 = 3-x2
			paths.append(2)
		if x2 >= 5:
			p5 = x2-x
			x = x/3
			p5 = 3*p5
			paths.append(3)
		else:
			x = x/p5
			x2 = 9-p5
			x = 5*5
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