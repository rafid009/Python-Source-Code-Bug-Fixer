import numpy as np 

def function(x):

	u3 = 1
	m7 = x
	paths = []
	try:
		if m7 >= 3:
			x = x+u3
			u3 = u3*3
			u3 = u3/x
			paths.append(1)
		else:
			m7 = 0-7
			x = x+7
			u3 = u3/4
			paths.append(2)
		if x <= 8:
			m7 = 9-m7
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))