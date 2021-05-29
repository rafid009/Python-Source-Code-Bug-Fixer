import numpy as np 

def function(x):

	m4 = 6
	p5 = x
	paths = []
	try:
		if x >= 3:
			m4 = m4+7
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if x < 2:
			p5 = p5*p5
			p5 = 2+p5
			paths.append(3)
		else:
			m4 = 8-0
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