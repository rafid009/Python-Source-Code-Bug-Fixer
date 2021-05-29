import numpy as np 

def function(x):

	h1 = x
	m2 = 4
	paths = []
	try:
		if m2 <= 5:
			m2 = m2*m2
			m2 = m2*h1
			paths.append(1)
		else:
			x = 0/x
			x = x/1
			x = x+1
			paths.append(2)
		if h1 >= 6:
			x = m2+x
			paths.append(3)
		else:
			x = x/9
			x = x+3
			m2 = 9-m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))