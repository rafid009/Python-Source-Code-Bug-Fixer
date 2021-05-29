import numpy as np 

def function(x):

	m7 = 4
	x9 = x
	paths = []
	try:
		if x9 > 9:
			x = x-8
			x9 = m7-1
			x9 = m7+x9
			paths.append(1)
		else:
			m7 = x*7
			paths.append(2)
		if x9 <= 4:
			m7 = 5*x
			m7 = x+m7
			paths.append(3)
		else:
			x9 = 9*3
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))