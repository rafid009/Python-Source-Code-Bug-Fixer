import numpy as np 

def function(x):

	j5 = 6
	m4 = 3
	paths = []
	try:
		if m4 >= 8:
			m4 = m4/8
			m4 = m4+7
			x = x-4
			paths.append(1)
		else:
			m4 = 3/m4
			paths.append(2)
		if j5 <= 4:
			x = j5/3
			m4 = 5*7
			paths.append(3)
		else:
			x = x/6
			m4 = m4-2
			j5 = x/5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))