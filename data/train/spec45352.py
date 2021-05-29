import numpy as np 

def function(x):

	m5 = 9
	t8 = 4
	paths = []
	try:
		if t8 <= 0:
			t8 = t8*x
			t8 = t8-x
			paths.append(1)
		else:
			x = x-t8
			m5 = m5+7
			paths.append(2)
		if m5 > 9:
			t8 = x-t8
			paths.append(3)
		else:
			m5 = x*m5
			m5 = 2/m5
			t8 = 5*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))