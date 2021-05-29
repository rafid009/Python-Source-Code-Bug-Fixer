import numpy as np 

def function(x):

	m7 = 1
	n3 = 5
	paths = []
	try:
		if x > 5:
			x = 2*9
			paths.append(1)
		else:
			m7 = m7-m7
			m7 = m7+m7
			x = n3+9
			paths.append(2)
		if n3 < 5:
			n3 = n3*6
			paths.append(3)
		else:
			n3 = 0*n3
			n3 = 6+2
			n3 = 5-n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))