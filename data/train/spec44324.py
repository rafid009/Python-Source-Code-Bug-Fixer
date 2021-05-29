import numpy as np 

def function(x):

	r3 = 3
	m1 = 5
	paths = []
	try:
		if x > 0:
			r3 = r3*m1
			x = r3/x
			r3 = m1+r3
			paths.append(1)
		else:
			m1 = m1/m1
			m1 = m1-m1
			r3 = r3/2
			paths.append(2)
		if x < 7:
			r3 = 5+0
			m1 = m1-8
			m1 = 7+m1
			paths.append(3)
		else:
			r3 = 3*5
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