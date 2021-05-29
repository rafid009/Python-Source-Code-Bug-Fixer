import numpy as np 

def function(x):

	m5 = 3
	b5 = x
	paths = []
	try:
		if m5 >= 4:
			m5 = m5*2
			x = x*x
			paths.append(1)
		else:
			m5 = b5/4
			x = 7*x
			paths.append(2)
		if x >= 4:
			b5 = b5-7
			m5 = 3*9
			paths.append(3)
		else:
			x = b5-x
			b5 = b5-b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))