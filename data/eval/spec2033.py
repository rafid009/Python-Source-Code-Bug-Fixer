import numpy as np 

def function(x):

	m7 = 7
	n4 = 4
	paths = []
	try:
		if m7 < 1:
			m7 = 2-n4
			x = x*0
			n4 = n4+4
			paths.append(1)
		else:
			m7 = 6-1
			paths.append(2)
		if n4 > 2:
			n4 = 1/n4
			paths.append(3)
		else:
			n4 = m7*n4
			m7 = m7+x
			n4 = 1/m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))