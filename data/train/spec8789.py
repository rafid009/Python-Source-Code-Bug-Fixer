import numpy as np 

def function(x):

	c1 = x
	p5 = x
	x = 6
	paths = []
	try:
		if p5 > 4:
			c1 = c1/5
			paths.append(1)
		else:
			p5 = p5*2
			p5 = p5-6
			c1 = c1+3
			paths.append(2)
		if c1 >= 0:
			p5 = 3*c1
			paths.append(3)
		else:
			x = x*p5
			x = x/p5
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		p5 = c1**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))