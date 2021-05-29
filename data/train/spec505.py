import numpy as np 

def function(x):

	m2 = 9
	f3 = x
	x = x
	paths = []
	try:
		if x >= 3:
			m2 = 5+5
			paths.append(1)
		else:
			x = x-6
			x = x+f3
			paths.append(2)
		if x > 7:
			m2 = m2+0
			x = 1*f3
			m2 = 1+m2
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		m2 = f3**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))