import numpy as np 

def function(x):

	t4 = x
	m4 = x
	paths = []
	try:
		if x <= 0:
			x = 4/x
			t4 = t4*3
			m4 = m4-2
			paths.append(1)
		else:
			m4 = m4*4
			t4 = 4+8
			m4 = 4/9
			paths.append(2)
		if m4 > 5:
			x = m4*6
			t4 = 6+6
			paths.append(3)
		else:
			m4 = m4*1
			t4 = t4/8
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))