import numpy as np 

def function(x):

	m8 = x
	t7 = 9
	paths = []
	try:
		if x >= 1:
			m8 = 5+m8
			t7 = t7/7
			paths.append(1)
		else:
			m8 = m8*7
			x = x*7
			t7 = t7*x
			paths.append(2)
		if m8 >= 9:
			x = x-t7
			m8 = 4/x
			paths.append(3)
		else:
			x = x/3
			m8 = m8*1
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		t7 = m8**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))