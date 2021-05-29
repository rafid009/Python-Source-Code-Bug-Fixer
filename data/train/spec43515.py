import numpy as np 

def function(x):

	m7 = x
	j8 = 1
	paths = []
	try:
		if x >= 5:
			x = x*2
			m7 = m7*4
			x = 4/x
			paths.append(1)
		else:
			j8 = 6/6
			x = 7-x
			paths.append(2)
		if x >= 0:
			m7 = m7/8
			paths.append(3)
		else:
			x = x-0
			x = x/x
			m7 = 7*x
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		j8 = m7**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))