import numpy as np 

def function(x):

	m9 = 4
	a9 = 9
	paths = []
	try:
		if m9 < 8:
			m9 = 5-m9
			paths.append(1)
		else:
			a9 = m9/a9
			x = m9+x
			x = m9/6
			paths.append(2)
		if x <= 7:
			a9 = 5-a9
			a9 = a9*7
			x = 6-x
			paths.append(3)
		else:
			x = x*2
			a9 = 8/1
			m9 = 1-m9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		m9 = a9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))