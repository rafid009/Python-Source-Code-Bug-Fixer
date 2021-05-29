import numpy as np 

def function(x):

	m5 = x
	f9 = x
	paths = []
	try:
		if m5 >= 1:
			x = 6/x
			x = m5*m5
			paths.append(1)
		else:
			m5 = 1*1
			paths.append(2)
		if m5 >= 7:
			f9 = 5-f9
			paths.append(3)
		else:
			f9 = f9+f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))