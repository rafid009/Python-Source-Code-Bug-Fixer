import numpy as np 

def function(x):

	j7 = x
	m7 = 2
	x = x
	paths = []
	try:
		if m7 < 0:
			x = 5+8
			paths.append(1)
		else:
			m7 = m7+0
			j7 = 2-j7
			m7 = m7+x
			paths.append(2)
		if x <= 4:
			m7 = 4*8
			m7 = 6/4
			m7 = j7/m7
			paths.append(3)
		else:
			j7 = j7*3
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))