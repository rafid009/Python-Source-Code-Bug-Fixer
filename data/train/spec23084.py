import numpy as np 

def function(x):

	n1 = x
	m1 = 0
	paths = []
	try:
		if m1 > 9:
			x = x*n1
			n1 = 0+n1
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if x >= 1:
			m1 = x-n1
			x = m1+x
			m1 = m1/3
			paths.append(3)
		else:
			x = x*0
			n1 = n1*3
			x = x-8
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))