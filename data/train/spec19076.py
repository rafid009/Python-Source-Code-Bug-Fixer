import numpy as np 

def function(x):

	k2 = 9
	m1 = x
	paths = []
	try:
		if m1 > 2:
			x = x-1
			k2 = 7+k2
			paths.append(1)
		else:
			k2 = k2+7
			paths.append(2)
		if m1 >= 7:
			x = k2-m1
			m1 = k2/8
			k2 = k2-8
			paths.append(3)
		else:
			x = x/m1
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