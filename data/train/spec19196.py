import numpy as np 

def function(x):

	m4 = 9
	b5 = 0
	paths = []
	try:
		if m4 >= 5:
			m4 = m4/5
			x = 3-b5
			paths.append(1)
		else:
			x = b5*x
			x = x/8
			b5 = 2-6
			paths.append(2)
		if b5 > 5:
			x = 6+1
			b5 = 0/x
			b5 = b5+m4
			paths.append(3)
		else:
			x = x*9
			m4 = 7-m4
			m4 = 4-m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))