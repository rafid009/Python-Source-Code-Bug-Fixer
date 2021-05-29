import numpy as np 

def function(x):

	m8 = 6
	t2 = 9
	paths = []
	try:
		if t2 > 5:
			t2 = t2*m8
			paths.append(1)
		else:
			t2 = t2+m8
			paths.append(2)
		if t2 < 8:
			m8 = x+m8
			paths.append(3)
		else:
			t2 = x/5
			x = 9+x
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