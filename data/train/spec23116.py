import numpy as np 

def function(x):

	t4 = 4
	m3 = 6
	paths = []
	try:
		if x >= 0:
			m3 = m3-9
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if m3 > 5:
			x = x/6
			t4 = 2*t4
			paths.append(3)
		else:
			m3 = 8*m3
			t4 = m3/t4
			m3 = 2-m3
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