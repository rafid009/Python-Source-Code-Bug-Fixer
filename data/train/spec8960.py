import numpy as np 

def function(x):

	p5 = 2
	m4 = x
	paths = []
	try:
		if p5 > 0:
			m4 = 2/p5
			m4 = m4/x
			paths.append(1)
		else:
			p5 = 4+8
			paths.append(2)
		if x <= 1:
			p5 = 8*p5
			m4 = m4+m4
			paths.append(3)
		else:
			m4 = m4/9
			p5 = 5-2
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