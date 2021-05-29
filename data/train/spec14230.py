import numpy as np 

def function(x):

	m7 = x
	p5 = 8
	paths = []
	try:
		if m7 >= 0:
			m7 = 2+m7
			paths.append(1)
		else:
			m7 = m7-8
			paths.append(2)
		if x > 4:
			x = m7-9
			m7 = 1+m7
			paths.append(3)
		else:
			p5 = p5*4
			x = x*x
			m7 = m7+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))