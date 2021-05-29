import numpy as np 

def function(x):

	i1 = 5
	m9 = x
	paths = []
	try:
		if i1 > 2:
			m9 = m9-9
			paths.append(1)
		else:
			x = m9*2
			i1 = 3*2
			paths.append(2)
		if x > 2:
			m9 = i1*m9
			i1 = 7+4
			x = x*x
			paths.append(3)
		else:
			i1 = 3*i1
			m9 = 8+m9
			i1 = x+m9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))