import numpy as np 

def function(x):

	t2 = 4
	m4 = 5
	paths = []
	try:
		if t2 < 4:
			x = x*0
			t2 = 3/x
			paths.append(1)
		else:
			m4 = t2/1
			m4 = 4-6
			t2 = 5/t2
			paths.append(2)
		if x < 6:
			t2 = 2/t2
			paths.append(3)
		else:
			x = m4*m4
			x = 3*2
			t2 = t2/t2
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))