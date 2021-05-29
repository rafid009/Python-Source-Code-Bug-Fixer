import numpy as np 

def function(x):

	t2 = 6
	m2 = 5
	paths = []
	try:
		if m2 < 3:
			x = m2/1
			x = 6-x
			x = x+1
			paths.append(1)
		else:
			m2 = 8-x
			t2 = t2+5
			m2 = m2*9
			paths.append(2)
		if x < 1:
			m2 = x/9
			t2 = 9-t2
			m2 = 9/x
			paths.append(3)
		else:
			t2 = 6+t2
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