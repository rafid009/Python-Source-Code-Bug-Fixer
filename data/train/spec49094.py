import numpy as np 

def function(x):

	u1 = x
	p5 = 8
	paths = []
	try:
		if x <= 5:
			u1 = u1+1
			u1 = u1-8
			p5 = p5*x
			paths.append(1)
		else:
			u1 = 5*x
			u1 = p5+p5
			paths.append(2)
		if x < 0:
			p5 = p5-x
			u1 = u1*5
			paths.append(3)
		else:
			p5 = p5/8
			x = x*7
			u1 = 6*u1
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