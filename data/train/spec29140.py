import numpy as np 

def function(x):

	n0 = x
	m5 = x
	paths = []
	try:
		if x > 8:
			n0 = 5/m5
			x = 1*x
			n0 = n0-7
			paths.append(1)
		else:
			n0 = n0/5
			x = 7-x
			paths.append(2)
		if x > 4:
			m5 = m5*0
			paths.append(3)
		else:
			n0 = n0+3
			x = n0*9
			n0 = n0/6
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		m5 = n0**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))