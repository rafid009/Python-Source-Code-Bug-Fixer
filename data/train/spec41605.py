import numpy as np 

def function(x):

	p7 = 5
	m9 = x
	paths = []
	try:
		if m9 <= 4:
			p7 = 9/9
			paths.append(1)
		else:
			x = 3/m9
			paths.append(2)
		if x > 4:
			m9 = 1+8
			p7 = p7+6
			m9 = 5-m9
			paths.append(3)
		else:
			x = x-2
			p7 = p7-3
			x = 8*m9
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		p7 = m9**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))