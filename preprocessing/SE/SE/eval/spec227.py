import numpy as np 

def function(x):

	m1 = 7
	j1 = 5
	paths = []
	try:
		if m1 <= 2:
			m1 = 3/m1
			j1 = j1/3
			m1 = m1*m1
			paths.append(1)
		else:
			m1 = m1-m1
			j1 = j1-7
			x = x*m1
			paths.append(2)
		if x >= 9:
			x = 2+x
			paths.append(3)
		else:
			m1 = j1/5
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))