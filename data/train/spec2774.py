import numpy as np 

def function(x):

	t7 = 7
	m9 = 1
	paths = []
	try:
		if m9 < 9:
			x = t7-8
			paths.append(1)
		else:
			x = 9-x
			x = 5-7
			paths.append(2)
		if t7 >= 4:
			t7 = x*1
			t7 = 8+t7
			t7 = 6-9
			paths.append(3)
		else:
			x = 6+9
			m9 = m9*x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		m9 = t7**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))