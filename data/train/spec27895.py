import numpy as np 

def function(x):

	m0 = 3
	t3 = x
	paths = []
	try:
		if m0 < 0:
			x = m0+m0
			x = x+2
			paths.append(1)
		else:
			m0 = m0*t3
			paths.append(2)
		if x <= 0:
			t3 = t3/1
			m0 = m0+m0
			paths.append(3)
		else:
			t3 = t3+m0
			t3 = t3/5
			x = x/7
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))