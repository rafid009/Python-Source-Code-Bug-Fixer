import numpy as np 

def function(x):

	t2 = x
	m1 = 8
	paths = []
	try:
		if m1 < 7:
			m1 = 7-m1
			t2 = 3+t2
			m1 = m1/9
			paths.append(1)
		else:
			t2 = t2*m1
			t2 = t2/3
			paths.append(2)
		if m1 > 6:
			m1 = m1*5
			x = x-t2
			t2 = 4-t2
			paths.append(3)
		else:
			t2 = 3/9
			t2 = x*4
			m1 = m1-t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))