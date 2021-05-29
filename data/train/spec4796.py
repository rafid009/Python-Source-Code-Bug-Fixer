import numpy as np 

def function(x):

	m1 = 1
	y7 = 3
	paths = []
	try:
		if m1 > 9:
			y7 = m1*0
			paths.append(1)
		else:
			m1 = m1-4
			m1 = 1*m1
			x = x-m1
			paths.append(2)
		if x > 5:
			x = x-2
			paths.append(3)
		else:
			y7 = m1/6
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