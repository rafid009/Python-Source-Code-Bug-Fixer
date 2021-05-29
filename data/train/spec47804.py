import numpy as np 

def function(x):

	m1 = 6
	r5 = x
	paths = []
	try:
		if x <= 2:
			m1 = 0*m1
			m1 = 0-5
			paths.append(1)
		else:
			x = x-1
			r5 = r5-9
			r5 = r5*5
			paths.append(2)
		if r5 >= 3:
			m1 = m1*7
			paths.append(3)
		else:
			r5 = 4*3
			x = m1+x
			m1 = m1-2
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