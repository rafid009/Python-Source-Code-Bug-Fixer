import numpy as np 

def function(x):

	m7 = 1
	n7 = 3
	paths = []
	try:
		if n7 <= 3:
			x = 0+4
			n7 = n7*7
			paths.append(1)
		else:
			m7 = 3+1
			paths.append(2)
		if x < 7:
			m7 = 1-8
			paths.append(3)
		else:
			m7 = 1*9
			n7 = m7/n7
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