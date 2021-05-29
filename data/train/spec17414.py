import numpy as np 

def function(x):

	t4 = 7
	m1 = 0
	paths = []
	try:
		if m1 <= 1:
			m1 = 4-m1
			x = 7-5
			paths.append(1)
		else:
			t4 = 9/t4
			x = 1/3
			m1 = m1-x
			paths.append(2)
		if m1 < 5:
			m1 = m1-8
			t4 = t4*m1
			x = x+5
			paths.append(3)
		else:
			x = m1+3
			m1 = x-m1
			t4 = t4/t4
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))