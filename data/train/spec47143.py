import numpy as np 

def function(x):

	m7 = x
	t2 = 3
	paths = []
	try:
		if x >= 1:
			x = x+x
			paths.append(1)
		else:
			t2 = 1-t2
			paths.append(2)
		if t2 <= 5:
			t2 = t2+3
			paths.append(3)
		else:
			m7 = m7/7
			m7 = 3*5
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		t2 = m7**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))