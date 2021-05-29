import numpy as np 

def function(x):

	t1 = x
	m8 = 3
	paths = []
	try:
		if x >= 4:
			t1 = m8*t1
			t1 = t1+8
			paths.append(1)
		else:
			m8 = t1*2
			paths.append(2)
		if m8 > 0:
			x = 0*7
			paths.append(3)
		else:
			t1 = 1+t1
			m8 = 3*1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		m8 = t1**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))