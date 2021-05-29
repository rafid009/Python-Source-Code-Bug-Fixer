import numpy as np 

def function(x):

	b2 = x
	m4 = 0
	paths = []
	try:
		if x < 1:
			b2 = 1-2
			paths.append(1)
		else:
			m4 = x*0
			m4 = 1*m4
			m4 = 3-m4
			paths.append(2)
		if m4 > 4:
			x = x+x
			paths.append(3)
		else:
			x = 7+x
			m4 = m4-b2
			x = x-1
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))