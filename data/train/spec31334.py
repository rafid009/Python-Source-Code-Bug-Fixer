import numpy as np 

def function(x):

	m5 = x
	n2 = 1
	paths = []
	try:
		if x < 4:
			n2 = m5*6
			x = 7+4
			paths.append(1)
		else:
			m5 = 0/x
			m5 = m5/x
			paths.append(2)
		if m5 >= 8:
			x = x-9
			x = x*x
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		n2 = m5**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))