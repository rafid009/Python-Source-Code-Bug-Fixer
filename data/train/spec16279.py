import numpy as np 

def function(x):

	b7 = x
	m9 = x
	paths = []
	try:
		if x > 7:
			m9 = m9*m9
			x = 3+x
			b7 = x+b7
			paths.append(1)
		else:
			m9 = 3-m9
			paths.append(2)
		if x <= 1:
			m9 = m9/b7
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))