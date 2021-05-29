import numpy as np 

def function(x):

	m5 = 9
	p3 = x
	paths = []
	try:
		if m5 > 7:
			x = x-9
			m5 = 4+m5
			paths.append(1)
		else:
			x = p3-9
			m5 = 5+6
			paths.append(2)
		if m5 < 7:
			x = 7*x
			paths.append(3)
		else:
			x = p3*x
			x = x+9
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))