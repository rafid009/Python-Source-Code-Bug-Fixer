import numpy as np 

def function(x):

	n4 = 2
	m7 = x
	paths = []
	try:
		if x <= 7:
			m7 = m7*2
			m7 = m7*4
			paths.append(1)
		else:
			m7 = m7-3
			m7 = 3/x
			paths.append(2)
		if n4 >= 5:
			m7 = m7-1
			n4 = 1+n4
			n4 = 9*0
			paths.append(3)
		else:
			n4 = m7-4
			m7 = 5-8
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