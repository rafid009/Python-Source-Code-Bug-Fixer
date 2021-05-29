import numpy as np 

def function(x):

	m7 = 1
	b8 = x
	paths = []
	try:
		if x < 0:
			x = 7-x
			m7 = m7-0
			paths.append(1)
		else:
			b8 = m7+b8
			b8 = b8/b8
			b8 = b8-6
			paths.append(2)
		if x < 1:
			x = x/6
			b8 = b8*7
			paths.append(3)
		else:
			x = x+0
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))