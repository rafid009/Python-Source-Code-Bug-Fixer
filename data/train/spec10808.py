import numpy as np 

def function(x):

	m0 = 6
	t3 = 5
	paths = []
	try:
		if t3 <= 5:
			t3 = 6-x
			paths.append(1)
		else:
			t3 = t3/t3
			x = 9-9
			paths.append(2)
		if t3 > 2:
			t3 = 1-t3
			t3 = t3/x
			t3 = 2*t3
			paths.append(3)
		else:
			x = x/m0
			x = 4*0
			m0 = m0/4
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		m0 = t3**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))