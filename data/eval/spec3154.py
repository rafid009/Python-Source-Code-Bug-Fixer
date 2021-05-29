import numpy as np 

def function(x):

	m5 = x
	t4 = 6
	paths = []
	try:
		if x >= 7:
			t4 = m5+5
			m5 = 6*8
			paths.append(1)
		else:
			x = x+0
			x = t4-x
			paths.append(2)
		if x < 5:
			x = x/t4
			t4 = t4/x
			paths.append(3)
		else:
			x = x*m5
			m5 = m5-m5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))