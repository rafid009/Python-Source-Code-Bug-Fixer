import numpy as np 

def function(x):

	t2 = 7
	m2 = 1
	paths = []
	try:
		if x < 1:
			m2 = m2/x
			paths.append(1)
		else:
			t2 = 4/t2
			t2 = t2+0
			paths.append(2)
		if x < 7:
			m2 = m2*1
			t2 = t2/5
			paths.append(3)
		else:
			t2 = x*t2
			m2 = 1-m2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))