import numpy as np 

def function(x):

	m1 = x
	b8 = 8
	paths = []
	try:
		if b8 <= 8:
			x = x*b8
			b8 = x*6
			b8 = b8*2
			paths.append(1)
		else:
			m1 = 2/m1
			x = x*0
			m1 = m1/6
			paths.append(2)
		if x < 2:
			m1 = m1+2
			paths.append(3)
		else:
			b8 = 0*x
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