import numpy as np 

def function(x):

	m1 = 4
	t9 = x
	x = 6
	paths = []
	try:
		if m1 > 3:
			m1 = 5+m1
			paths.append(1)
		else:
			m1 = 8*7
			t9 = 6-1
			t9 = 2+t9
			paths.append(2)
		if x > 6:
			x = x+3
			x = x/m1
			paths.append(3)
		else:
			x = m1-9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))