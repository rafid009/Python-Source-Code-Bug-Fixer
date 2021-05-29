import numpy as np 

def function(x):

	n1 = x
	m5 = x
	paths = []
	try:
		if n1 < 4:
			x = 1/x
			m5 = m5*m5
			paths.append(1)
		else:
			n1 = n1-9
			m5 = 4+x
			n1 = n1+n1
			paths.append(2)
		if m5 <= 0:
			m5 = m5-n1
			paths.append(3)
		else:
			m5 = 5*x
			n1 = m5-n1
			n1 = 8/n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))