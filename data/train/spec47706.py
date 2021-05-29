import numpy as np 

def function(x):

	m2 = 7
	p3 = x
	paths = []
	try:
		if p3 >= 7:
			x = m2-x
			m2 = m2/9
			paths.append(1)
		else:
			x = 1/4
			paths.append(2)
		if x < 4:
			x = x*2
			paths.append(3)
		else:
			p3 = p3/8
			x = 4*x
			m2 = 8+0
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))