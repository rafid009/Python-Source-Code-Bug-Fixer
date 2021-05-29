import numpy as np 

def function(x):

	p5 = 9
	m2 = x
	paths = []
	try:
		if p5 > 3:
			p5 = m2-x
			p5 = m2*p5
			m2 = m2-x
			paths.append(1)
		else:
			p5 = p5-9
			p5 = 7*x
			p5 = p5/2
			paths.append(2)
		if p5 >= 8:
			x = x*7
			paths.append(3)
		else:
			m2 = m2/6
			p5 = x/4
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		m2 = p5**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))