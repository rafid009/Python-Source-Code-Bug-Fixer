import numpy as np 

def function(x):

	y4 = x
	m3 = x
	paths = []
	try:
		if y4 >= 0:
			y4 = y4/2
			x = x*1
			y4 = m3+6
			paths.append(1)
		else:
			m3 = m3-7
			x = 0*x
			y4 = 7+6
			paths.append(2)
		if x >= 0:
			y4 = y4+4
			m3 = m3/6
			m3 = m3*3
			paths.append(3)
		else:
			x = m3/9
			y4 = m3+6
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		y4 = m3**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))