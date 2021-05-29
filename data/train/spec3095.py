import numpy as np 

def function(x):

	m4 = 0
	t7 = x
	paths = []
	try:
		if x <= 4:
			x = 9/6
			m4 = 5+m4
			paths.append(1)
		else:
			m4 = m4-x
			x = x-2
			t7 = 3*5
			paths.append(2)
		if m4 >= 5:
			x = x/m4
			m4 = m4+t7
			paths.append(3)
		else:
			t7 = t7/x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		m4 = t7**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))