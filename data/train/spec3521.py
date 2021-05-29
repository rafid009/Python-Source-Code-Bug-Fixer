import numpy as np 

def function(x):

	n2 = 9
	m9 = x
	paths = []
	try:
		if m9 > 9:
			n2 = 7/n2
			paths.append(1)
		else:
			x = n2+3
			paths.append(2)
		if n2 >= 5:
			m9 = m9-x
			paths.append(3)
		else:
			n2 = n2+2
			n2 = n2+m9
			x = x*m9
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))