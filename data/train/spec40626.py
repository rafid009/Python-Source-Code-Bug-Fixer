import numpy as np 

def function(x):

	b9 = 5
	m7 = 6
	paths = []
	try:
		if m7 <= 5:
			m7 = m7+2
			b9 = b9+0
			b9 = x+3
			paths.append(1)
		else:
			x = 6+x
			x = x-5
			paths.append(2)
		if b9 <= 3:
			b9 = m7*b9
			m7 = m7+7
			x = x-4
			paths.append(3)
		else:
			b9 = b9*x
			b9 = b9*6
			m7 = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))