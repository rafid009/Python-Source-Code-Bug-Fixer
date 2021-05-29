import numpy as np 

def function(x):

	m5 = 1
	b4 = x
	paths = []
	try:
		if b4 <= 5:
			m5 = 3+m5
			m5 = x*3
			paths.append(1)
		else:
			x = 8+6
			paths.append(2)
		if x < 5:
			b4 = b4*m5
			paths.append(3)
		else:
			m5 = 0*m5
			m5 = 4*x
			x = b4+b4
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		b4 = m5**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))