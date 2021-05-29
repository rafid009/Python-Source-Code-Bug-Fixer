import numpy as np 

def function(x):

	n4 = 9
	m8 = x
	x = 6
	paths = []
	try:
		if n4 >= 6:
			x = 9-6
			paths.append(1)
		else:
			x = 4*x
			n4 = 5*n4
			paths.append(2)
		if m8 > 5:
			x = x+9
			n4 = n4/n4
			paths.append(3)
		else:
			x = x*0
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))