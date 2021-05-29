import numpy as np 

def function(x):

	t3 = 9
	m5 = 7
	paths = []
	try:
		if x <= 0:
			m5 = m5*4
			m5 = m5*3
			m5 = m5*5
			paths.append(1)
		else:
			t3 = t3/4
			paths.append(2)
		if t3 <= 7:
			t3 = t3+8
			m5 = t3*t3
			paths.append(3)
		else:
			t3 = t3+t3
			t3 = t3/t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))