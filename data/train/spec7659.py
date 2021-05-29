import numpy as np 

def function(x):

	t3 = 3
	m8 = x
	paths = []
	try:
		if x > 2:
			x = 5+5
			x = 2-3
			t3 = t3/7
			paths.append(1)
		else:
			x = 6/x
			x = t3+3
			paths.append(2)
		if x <= 2:
			t3 = t3*0
			paths.append(3)
		else:
			x = x/m8
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))