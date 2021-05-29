import numpy as np 

def function(x):

	t2 = 3
	m9 = 0
	x = x
	paths = []
	try:
		if x <= 4:
			x = x+x
			paths.append(1)
		else:
			m9 = 2+m9
			paths.append(2)
		if x < 2:
			m9 = m9/8
			t2 = t2-t2
			paths.append(3)
		else:
			t2 = t2/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))