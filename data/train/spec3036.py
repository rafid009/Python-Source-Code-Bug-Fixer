import numpy as np 

def function(x):

	m5 = x
	n1 = 4
	paths = []
	try:
		if n1 >= 8:
			m5 = m5*5
			m5 = n1*m5
			paths.append(1)
		else:
			m5 = m5-5
			n1 = n1*1
			x = 2+x
			paths.append(2)
		if n1 <= 5:
			m5 = 5/m5
			paths.append(3)
		else:
			n1 = n1/n1
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))