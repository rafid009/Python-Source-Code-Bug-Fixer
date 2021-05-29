import numpy as np 

def function(x):

	m1 = 3
	g8 = x
	paths = []
	try:
		if x >= 5:
			m1 = m1-x
			x = x*0
			x = m1-g8
			paths.append(1)
		else:
			m1 = 8+x
			paths.append(2)
		if m1 > 7:
			x = m1+7
			x = m1+5
			paths.append(3)
		else:
			g8 = x-8
			x = x*5
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))